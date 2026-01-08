---
title: "Node: ServiceNow"
slug: "node-servicenow"
version: "1"
updated: "2026-01-08"
summary: "Consume ServiceNow API"
node_type: "regular"
group: "['output']"
---

# Node: ServiceNow

**Purpose.** Consume ServiceNow API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:servicenow.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **serviceNowOAuth2Api**: N/A
- **serviceNowBasicApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `serviceNowOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |
| `serviceNowBasicApi` | ✓ | {'show': {'authentication': ['basicAuth']}} |

---

## Operations

### Attachment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Upload | `upload` | Upload an attachment to a specific table record |
| Delete | `delete` | Delete an attachment |
| Get | `get` | Get an attachment |
| Get Many | `getAll` | Get many attachments on a table |

### Businessservice Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many business services |

### Configurationitems Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many configuration items |

### Department Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many departments |

### Dictionary Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many dictionaries |

### Incident Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an incident |
| Delete | `delete` | Delete an incident |
| Get | `get` | Get an incident |
| Get Many | `getAll` | Get many incidents |
| Update | `update` | Update an incident |

### Tablerecord Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a table record |
| Delete | `delete` | Delete a table record |
| Get | `get` | Get a table record |
| Get Many | `getAll` | Get many table records |
| Update | `update` | Update a table record |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a user |
| Delete | `delete` | Delete a user |
| Get | `get` | Get a user |
| Get Many | `getAll` | Get many users |
| Update | `update` | Update a user |

### Usergroup Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many user groups |

### Userrole Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many user roles |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | user | ✗ | Resource to operate on |  |

**Resource options:**

* **Attachment** (`attachment`)
* **Business Service** (`businessService`)
* **Configuration Item** (`configurationItems`)
* **Department** (`department`)
* **Dictionary** (`dictionary`)
* **Incident** (`incident`)
* **Table Record** (`tableRecord`)
* **User** (`user`)
* **User Group** (`userGroup`)
* **User Role** (`userRole`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | upload | ✗ | Upload an attachment to a specific table record |  |

**Operation options:**

* **Upload** (`upload`) - Upload an attachment to a specific table record
* **Delete** (`delete`) - Delete an attachment
* **Get** (`get`) - Get an attachment
* **Get Many** (`getAll`) - Get many attachments on a table

---

### Upload parameters (`upload`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table Name or ID | `tableName` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Table Record ID | `id` | string |  | ✓ | Sys_id of the record in the table specified in Table Name that you want to attach the file to |  |
| Input Data Field Name | `inputDataFieldName` | string | data | ✓ | Name of the binary property that contains the data to upload |  |
| Options | `options` | collection | {} | ✗ | Name to give the attachment | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| File Name for the Attachment | `file_name` | string |  | Name to give the attachment |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Attachment ID | `attachmentId` | string |  | ✓ | Sys_id value of the attachment to delete |  |
| Incident ID | `id` | string |  | ✓ | Unique identifier of the incident |  |
| Table Name or ID | `tableName` | options |  | ✓ | Name of the table in which the record exists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Table Record ID | `id` | string |  | ✓ | Unique identifier of the record |  |
| User ID | `id` | string |  | ✓ | Unique identifier of the user |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Attachment ID | `attachmentId` | string |  | ✓ | Sys_id value of the attachment to delete |  |
| Download Attachments | `download` | boolean | False | ✓ |  |  |
| Output Field | `outputField` | string | data | ✗ | Field name where downloaded data will be placed |  |
| Options | `options` | collection | {} | ✗ | An encoded query string used to filter the results | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filter | `queryFilter` | string |  | An encoded query string used to filter the results |

</details>

| Incident ID | `id` | string |  | ✓ | Unique identifier of the incident |  |
| Options | `options` | collection | {} | ✗ | Whether to exclude Table API links for reference fields | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exclude Reference Link | `sysparm_exclude_reference_link` | boolean | False | Whether to exclude Table API links for reference fields |
| Field Names or IDs | `sysparm_fields` | multiOptions | [] | A list of fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Return Values | `sysparm_display_value` | options | false | Choose which values to return |

</details>

| Table Name or ID | `tableName` | options |  | ✓ | Name of the table in which the record exists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Table Record ID | `id` | string |  | ✓ | Unique identifier of the record |  |
| Options | `options` | collection | {} | ✗ | Whether to exclude Table API links for reference fields | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exclude Reference Link | `sysparm_exclude_reference_link` | boolean | False | Whether to exclude Table API links for reference fields |
| Field Names or IDs | `sysparm_fields` | multiOptions | [] | A list of fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Return Values | `sysparm_display_value` | options | false | Choose which values to return |

</details>

| Retrieve Identifier | `getOption` | options | id | ✓ | Unique identifier of the user |  |

**Retrieve Identifier options:**

* **ID** (`id`)
* **Username** (`user_name`)

| Username | `user_name` | string |  | ✓ | Unique identifier of the user |  |
| User ID | `id` | string |  | ✓ | Unique identifier of the user |  |
| Options | `options` | collection | {} | ✗ | Whether to exclude Table API links for reference fields | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exclude Reference Link | `sysparm_exclude_reference_link` | boolean | False | Whether to exclude Table API links for reference fields |
| Field Names or IDs | `sysparm_fields` | multiOptions | [] | A list of fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Return Values | `sysparm_display_value` | options | false | Choose which values to return |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Table Name or ID | `tableName` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Download Attachments | `download` | boolean | False | ✓ |  |  |
| Output Field | `outputField` | string | data | ✗ | Field name where downloaded data will be placed |  |
| Options | `options` | collection | {} | ✗ | An encoded query string used to filter the results | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filter | `queryFilter` | string |  | An encoded query string used to filter the results |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Whether to exclude Table API links for reference fields | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exclude Reference Link | `sysparm_exclude_reference_link` | boolean | False | Whether to exclude Table API links for reference fields |
| Field Names or IDs | `sysparm_fields` | multiOptions | [] | A list of fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Filter | `sysparm_query` | string |  | An encoded query string used to filter the results. <a href="https://developer.servicenow.com/dev.do#!/learn/learning-plans/quebec/servicenow_application_developer/app_store_learnv2_rest_quebec_more_about_query_parameters">More info</a>. |
| Return Values | `sysparm_display_value` | options | false | Choose which values to return |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Whether to exclude Table API links for reference fields | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exclude Reference Link | `sysparm_exclude_reference_link` | boolean | False | Whether to exclude Table API links for reference fields |
| Field Names or IDs | `sysparm_fields` | multiOptions | [] | A list of fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Filter | `sysparm_query` | string |  | An encoded query string used to filter the results. <a href="https://developer.servicenow.com/dev.do#!/learn/learning-plans/quebec/servicenow_application_developer/app_store_learnv2_rest_quebec_more_about_query_parameters">More info</a>. |
| Return Values | `sysparm_display_value` | options | false | Choose which values to return |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Whether to exclude Table API links for reference fields | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exclude Reference Link | `sysparm_exclude_reference_link` | boolean | False | Whether to exclude Table API links for reference fields |
| Field Names or IDs | `sysparm_fields` | multiOptions | [] | A list of fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Filter | `sysparm_query` | string |  | An encoded query string used to filter the results. <a href="https://developer.servicenow.com/dev.do#!/learn/learning-plans/quebec/servicenow_application_developer/app_store_learnv2_rest_quebec_more_about_query_parameters">More info</a>. |
| Return Values | `sysparm_display_value` | options | false | Choose which values to return |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Whether to exclude Table API links for reference fields | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exclude Reference Link | `sysparm_exclude_reference_link` | boolean | False | Whether to exclude Table API links for reference fields |
| Field Names or IDs | `sysparm_fields` | multiOptions | [] | A list of fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Filter | `sysparm_query` | string |  | An encoded query string used to filter the results. <a href="https://developer.servicenow.com/dev.do#!/learn/learning-plans/quebec/servicenow_application_developer/app_store_learnv2_rest_quebec_more_about_query_parameters">More info</a>. |
| Return Values | `sysparm_display_value` | options | false | Choose which values to return |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Whether to exclude Table API links for reference fields | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exclude Reference Link | `sysparm_exclude_reference_link` | boolean | False | Whether to exclude Table API links for reference fields |
| Field Names or IDs | `sysparm_fields` | multiOptions | [] | A list of fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Filter | `sysparm_query` | string |  | An encoded query string used to filter the results. <a href="https://developer.servicenow.com/dev.do#!/learn/learning-plans/quebec/servicenow_application_developer/app_store_learnv2_rest_quebec_more_about_query_parameters">More info</a>. |
| Return Values | `sysparm_display_value` | options | false | Choose which values to return |

</details>

| Table Name or ID | `tableName` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Whether to exclude Table API links for reference fields | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exclude Reference Link | `sysparm_exclude_reference_link` | boolean | False | Whether to exclude Table API links for reference fields |
| Field Names or IDs | `sysparm_fields` | multiOptions | [] | A list of fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Filter | `sysparm_query` | string |  | An encoded query string used to filter the results. <a href="https://developer.servicenow.com/dev.do#!/learn/learning-plans/quebec/servicenow_application_developer/app_store_learnv2_rest_quebec_more_about_query_parameters">More info</a>. |
| Return Values | `sysparm_display_value` | options | false | Choose which values to return |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Whether to exclude Table API links for reference fields | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exclude Reference Link | `sysparm_exclude_reference_link` | boolean | False | Whether to exclude Table API links for reference fields |
| Field Names or IDs | `sysparm_fields` | multiOptions | [] | A list of fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Filter | `sysparm_query` | string |  | An encoded query string used to filter the results. <a href="https://developer.servicenow.com/dev.do#!/learn/learning-plans/quebec/servicenow_application_developer/app_store_learnv2_rest_quebec_more_about_query_parameters">More info</a>. |
| Return Values | `sysparm_display_value` | options | false | Choose which values to return |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Whether to exclude Table API links for reference fields | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exclude Reference Link | `sysparm_exclude_reference_link` | boolean | False | Whether to exclude Table API links for reference fields |
| Field Names or IDs | `sysparm_fields` | multiOptions | [] | A list of fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Filter | `sysparm_query` | string |  | An encoded query string used to filter the results. <a href="https://developer.servicenow.com/dev.do#!/learn/learning-plans/quebec/servicenow_application_developer/app_store_learnv2_rest_quebec_more_about_query_parameters">More info</a>. |
| Return Values | `sysparm_display_value` | options | false | Choose which values to return |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |
| Options | `options` | collection | {} | ✗ | Whether to exclude Table API links for reference fields | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Exclude Reference Link | `sysparm_exclude_reference_link` | boolean | False | Whether to exclude Table API links for reference fields |
| Field Names or IDs | `sysparm_fields` | multiOptions | [] | A list of fields to return. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Filter | `sysparm_query` | string |  | An encoded query string used to filter the results. <a href="https://developer.servicenow.com/dev.do#!/learn/learning-plans/quebec/servicenow_application_developer/app_store_learnv2_rest_quebec_more_about_query_parameters">More info</a>. |
| Return Values | `sysparm_display_value` | options | false | Choose which values to return |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Short Description | `short_description` | string |  | ✓ | Short description of the incident |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Which user is the incident assigned to. Requires the selection of an assignment group. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assignee Name or ID | `assigned_to` | options |  | Which user is the incident assigned to. Requires the selection of an assignment group. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Assignment Group Name or ID | `assignment_group` | options |  | The assignment group of the incident. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Business Service Name or ID | `business_service` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Caller ID | `caller_id` | string |  | The unique identifier of the caller of the incident |
| Category Name or ID | `category` | options |  | The category of the incident. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Close Notes | `close_notes` | string |  | The close notes for the incident |
| Configuration Item Names or IDs | `cmdb_ci` | multiOptions | [] | Configuration Items, 'cmdb_ci' in metadata. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Contact Type | `contact_type` | options |  |  |
| Description | `description` | string |  | The description of the incident |
| Impact | `impact` | options | 1 | The impact of the incident |
| Resolution Code Name or ID | `close_code` | options |  | The resolution code of the incident, 'close_code' in metadata. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| State Name or ID | `state` | options |  | The state of the incident. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Subcategory Name or ID | `subcategory` | options |  | The subcategory of the incident. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Urgency | `urgency` | options | 1 | The urgency of the incident |

</details>

| Table Name or ID | `tableName` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Data to Send | `dataToSend` | options | columns | ✗ | Use when node input names match destination field names |  |

**Data to Send options:**

* **Auto-Map Input Data to Columns** (`mapInput`) - Use when node input names match destination field names
* **Define Below for Each Column** (`columns`) - Set the value for each destination column
* **Nothing** (`nothing`) - Don't send any column data

| Inputs to Ignore | `inputsToIgnore` | string |  | ✗ | List of input properties to avoid sending, separated by commas. Leave empty to send all inputs. |  |
| Fields to Send | `fieldsToSend` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add field to send |  |

<details>
<summary><strong>Fields to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field | `field` |  |  |  |

</details>

| Short Description | `short_description` | string |  | ✓ | Short description of the user |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether to activate the user | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Active | `active` | boolean | False | Whether to activate the user |
| Building | `building` | string |  | The Building address |
| City | `city` | string |  | City of the user |
| Company | `company` | string |  | The name of the company for the user |
| Country | `country` | string |  | Country of the user |
| Department | `department` | string |  | Department of the user |
| Email | `email` | string |  | The email address associated with the user |
| First Name | `first_name` | string |  | The first name of the user |
| Gender | `gender` | string |  | The gender of the user |
| Home Phone | `home_phone` | string |  | Home phone of the user |
| Last Name | `last_name` | string |  | The last name of the user |
| Location | `location` | string |  | Location of the user |
| Manager | `manager` | string |  | Manager of the user |
| Middle Name | `middle_name` | string |  | The middle name of the user |
| Mobile Phone | `mobile_phone` | string |  | Mobile phone number of the user |
| Password | `user_password` | string |  | The user's password |
| Password Needs Reset | `password_needs_reset` | boolean | False | Whether to require a password reset when the user logs in |
| Phone | `phone` | string |  | The main phone number of the user |
| Role Names or IDs | `roles` | multiOptions | [] | Roles of the user. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Source | `source` | string |  |  |
| State | `state` | string |  | State for the user |
| Street | `street` | string |  | Street information for the user separated by comma |
| Username | `user_name` | string |  | A username associated with the user (e.g. user_name.123) |
| Zip Code | `zip` | string |  | Zip code for the user |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Incident ID | `id` | string |  | ✓ | Unique identifier of the incident |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Which user is the incident assigned to. Requires the selection of an assignment group. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assigned To Name or ID | `assigned_to` | options |  | Which user is the incident assigned to. Requires the selection of an assignment group. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Assignment Group Name or ID | `assignment_group` | options |  | The assignment group of the incident. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Business Service Name or ID | `business_service` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Caller ID | `caller_id` | string |  | The unique identifier of the caller of the incident |
| Category Name or ID | `category` | options |  | The category of the incident. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Close Notes | `close_notes` | string |  | The close notes for the incident |
| Configuration Item Names or IDs | `cmdb_ci` | multiOptions | [] | Configuration Items, 'cmdb_ci' in metadata. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Contact Type | `contact_type` | options |  |  |
| Description | `description` | string |  | The description of the incident |
| Impact | `impact` | options | 1 | The impact of the incident |
| Resolution Code Name or ID | `close_code` | options |  | The resolution code of the incident. 'close_code' in metadata. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| On Hold Reason Name or ID | `hold_reason` | options |  | The on hold reason for the incident. It applies if the state is <code>On Hold</code>. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| State Name or ID | `state` | options |  | The state of the incident. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Subcategory Name or ID | `subcategory` | options |  | The subcategory of the incident. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Urgency | `urgency` | options | 1 | The urgency of the incident |
| Work Notes | `work_notes` | string |  | Work notes for the incident |

</details>

| Table Name or ID | `tableName` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Table Record ID | `id` | string |  | ✓ | Unique identifier of the record |  |
| Data to Send | `dataToSend` | options | columns | ✗ | Use when node input names match destination field names |  |

**Data to Send options:**

* **Auto-Map Input Data to Columns** (`mapInput`) - Use when node input names match destination field names
* **Define Below for Each Column** (`columns`) - Set the value for each destination column
* **Nothing** (`nothing`) - Don't send any column data

| Inputs to Ignore | `inputsToIgnore` | string |  | ✗ | List of input properties to avoid sending, separated by commas. Leave empty to send all inputs. |  |
| Fields to Send | `fieldsToSend` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add field to send |  |

<details>
<summary><strong>Fields to Send sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Field | `field` |  |  |  |

</details>

| User ID | `id` | string |  | ✓ | Unique identifier of the user |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Whether to activate the user | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Active | `active` | boolean | False | Whether to activate the user |
| Building | `building` | string |  | The Building address |
| City | `city` | string |  | City of the user |
| Company | `company` | string |  | The name of the company for the user |
| Country | `country` | string |  | Country of the user |
| Department | `department` | string |  | Department of the user |
| Email | `email` | string |  | The email address associated with the user |
| First Name | `first_name` | string |  | The first name of the user |
| Gender | `gender` | string |  | The gender of the user |
| Home Phone | `home_phone` | string |  | Home phone of the user |
| Last Name | `last_name` | string |  | The last name of the user |
| Location | `location` | string |  | Location of the user |
| Manager | `manager` | string |  | Manager of the user |
| Middle Name | `middle_name` | string |  | The middle name of the user |
| Mobile Phone | `mobile_phone` | string |  | Mobile phone number of the user |
| Password | `user_password` | string |  | The user's password |
| Password Needs Reset | `password_needs_reset` | boolean | False | Whether to require a password reset when the user logs in |
| Phone | `phone` | string |  | The main phone number of the user |
| Role Names or IDs | `roles` | multiOptions | [] | Roles of the user. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Source | `source` | string |  |  |
| State | `state` | string |  | State for the user |
| Street | `street` | string |  | Street information for the user separated by comma |
| Username | `user_name` | string |  | A username associated with the user (e.g. user_name.123) |
| Zip Code | `zip` | string |  | Zip code for the user |

</details>


---

## Load Options Methods

- `getTables`

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
* Categories: Productivity, Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: serviceNow
displayName: ServiceNow
description: Consume ServiceNow API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: serviceNowOAuth2Api
  required: true
- name: serviceNowBasicApi
  required: true
operations:
- id: upload
  name: Upload
  description: Upload an attachment to a specific table record
  params:
  - id: tableName
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - tableRecord
          operation:
          - update
    typeInfo: &id004
      type: options
      displayName: Table Name or ID
      name: tableName
      typeOptions:
        loadOptionsMethod: getTables
      possibleValues: []
  - id: id
    name: Table Record ID
    type: string
    default: ''
    required: true
    description: Sys_id of the record in the table specified in Table Name that you
      want to attach the file to
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - update
    typeInfo: &id002
      type: string
      displayName: User ID
      name: id
  - id: inputDataFieldName
    name: Input Data Field Name
    type: string
    default: data
    required: true
    description: Name of the binary property that contains the data to upload
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - attachment
          operation:
          - upload
    typeInfo:
      type: string
      displayName: Input Data Field Name
      name: inputDataFieldName
- id: delete
  name: Delete
  description: Delete an attachment
  params:
  - id: attachmentId
    name: Attachment ID
    type: string
    default: ''
    required: true
    description: Sys_id value of the attachment to delete
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - attachment
          operation:
          - get
    typeInfo: &id006
      type: string
      displayName: Attachment ID
      name: attachmentId
  - id: id
    name: Incident ID
    type: string
    default: ''
    required: true
    description: Unique identifier of the incident
    validation: *id001
    typeInfo: *id002
  - id: tableName
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: Name of the table in which the record exists. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Table Record ID
    type: string
    default: ''
    required: true
    description: Unique identifier of the record
    validation: *id001
    typeInfo: *id002
  - id: id
    name: User ID
    type: string
    default: ''
    required: true
    description: Unique identifier of the user
    validation: *id001
    typeInfo: *id002
- id: get
  name: Get
  description: Get an attachment
  params:
  - id: attachmentId
    name: Attachment ID
    type: string
    default: ''
    required: true
    description: Sys_id value of the attachment to delete
    validation: *id005
    typeInfo: *id006
  - id: download
    name: Download Attachments
    type: boolean
    default: false
    required: true
    description: ''
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - attachment
          operation:
          - get
          - getAll
    typeInfo: &id008
      type: boolean
      displayName: Download Attachments
      name: download
  - id: outputField
    name: Output Field
    type: string
    default: data
    required: false
    description: Field name where downloaded data will be placed
    validation: &id009
      displayOptions:
        show:
          resource:
          - attachment
          operation:
          - get
          - getAll
          download:
          - true
    typeInfo: &id010
      type: string
      displayName: Output Field
      name: outputField
  - id: id
    name: Incident ID
    type: string
    default: ''
    required: true
    description: Unique identifier of the incident
    validation: *id001
    typeInfo: *id002
  - id: tableName
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: Name of the table in which the record exists. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Table Record ID
    type: string
    default: ''
    required: true
    description: Unique identifier of the record
    validation: *id001
    typeInfo: *id002
  - id: getOption
    name: Retrieve Identifier
    type: options
    default: id
    required: true
    description: Unique identifier of the user
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
    typeInfo:
      type: options
      displayName: Retrieve Identifier
      name: getOption
      possibleValues:
      - value: id
        name: ID
        description: ''
      - value: user_name
        name: Username
        description: ''
  - id: user_name
    name: Username
    type: string
    default: ''
    required: true
    description: Unique identifier of the user
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
          getOption:
          - user_name
    typeInfo:
      type: string
      displayName: Username
      name: user_name
  - id: id
    name: User ID
    type: string
    default: ''
    required: true
    description: Unique identifier of the user
    validation: *id001
    typeInfo: *id002
- id: getAll
  name: Get Many
  description: Get many attachments on a table
  params:
  - id: tableName
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id011
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - userRole
    typeInfo: &id012
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id013
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - userRole
          returnAll:
          - false
    typeInfo: &id014
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: download
    name: Download Attachments
    type: boolean
    default: false
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: outputField
    name: Output Field
    type: string
    default: data
    required: false
    description: Field name where downloaded data will be placed
    validation: *id009
    typeInfo: *id010
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
  - id: tableName
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id011
    typeInfo: *id012
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
- id: create
  name: Create
  description: ''
  params:
  - id: short_description
    name: Short Description
    type: string
    default: ''
    required: true
    description: Short description of the incident
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - create
    typeInfo: &id016
      type: string
      displayName: Short Description
      name: short_description
  - id: tableName
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: dataToSend
    name: Data to Send
    type: options
    default: columns
    required: false
    description: Use when node input names match destination field names
    validation: &id017
      displayOptions:
        show:
          resource:
          - tableRecord
          operation:
          - update
    typeInfo: &id018
      type: options
      displayName: Data to Send
      name: dataToSend
      possibleValues:
      - value: mapInput
        name: Auto-Map Input Data to Columns
        description: Use when node input names match destination field names
      - value: columns
        name: Define Below for Each Column
        description: Set the value for each destination column
      - value: nothing
        name: Nothing
        description: Don't send any column data
  - id: inputsToIgnore
    name: Inputs to Ignore
    type: string
    default: ''
    required: false
    description: List of input properties to avoid sending, separated by commas. Leave
      empty to send all inputs.
    validation: &id019
      displayOptions:
        show:
          resource:
          - tableRecord
          operation:
          - update
          dataToSend:
          - mapInput
    typeInfo: &id020
      type: string
      displayName: Inputs to Ignore
      name: inputsToIgnore
  - id: fieldsToSend
    name: Fields to Send
    type: fixedCollection
    default: {}
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add field to send
    validation: &id021
      displayOptions:
        show:
          resource:
          - tableRecord
          operation:
          - update
          dataToSend:
          - columns
    typeInfo: &id022
      type: fixedCollection
      displayName: Fields to Send
      name: fieldsToSend
      typeOptions:
        multipleValues: true
      subProperties:
      - name: field
        displayName: Field
        values:
        - displayName: Field Name or ID
          name: column
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getColumns
        - displayName: Field Value
          name: value
          type: string
          default: ''
  - id: short_description
    name: Short Description
    type: string
    default: ''
    required: true
    description: Short description of the user
    validation: *id015
    typeInfo: *id016
- id: update
  name: Update
  description: ''
  params:
  - id: id
    name: Incident ID
    type: string
    default: ''
    required: true
    description: Unique identifier of the incident
    validation: *id001
    typeInfo: *id002
  - id: tableName
    name: Table Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id003
    typeInfo: *id004
  - id: id
    name: Table Record ID
    type: string
    default: ''
    required: true
    description: Unique identifier of the record
    validation: *id001
    typeInfo: *id002
  - id: dataToSend
    name: Data to Send
    type: options
    default: columns
    required: false
    description: Use when node input names match destination field names
    validation: *id017
    typeInfo: *id018
  - id: inputsToIgnore
    name: Inputs to Ignore
    type: string
    default: ''
    required: false
    description: List of input properties to avoid sending, separated by commas. Leave
      empty to send all inputs.
    validation: *id019
    typeInfo: *id020
  - id: fieldsToSend
    name: Fields to Send
    type: fixedCollection
    default: {}
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add field to send
    validation: *id021
    typeInfo: *id022
  - id: id
    name: User ID
    type: string
    default: ''
    required: true
    description: Unique identifier of the user
    validation: *id001
    typeInfo: *id002
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
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: updateFields
    text: Add Field
  - field: fieldsToSend
    text: Add field to send
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: fieldsToSend
    text: Add field to send
  - field: additionalFields
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  hints:
  - field: options
    text: All parameters are case-sensitive. Queries can contain more than one entry.
      <a href="https://developer.servicenow.com/dev.do#!/learn/learning-plans/quebec/servicenow_application_developer/app_store_learnv2_rest_quebec_more_about_query_parameters">More
      information</a>.
  - field: options
    text: String of comma separated values or an array of strings can be set in an
      expression
  - field: options
    text: String of comma separated values or an array of strings can be set in an
      expression
  - field: options
    text: String of comma separated values or an array of strings can be set in an
      expression
  - field: options
    text: String of comma separated values or an array of strings can be set in an
      expression
  - field: options
    text: String of comma separated values or an array of strings can be set in an
      expression
  - field: options
    text: String of comma separated values or an array of strings can be set in an
      expression
  - field: options
    text: String of comma separated values or an array of strings can be set in an
      expression
  - field: options
    text: String of comma separated values or an array of strings can be set in an
      expression
  - field: options
    text: String of comma separated values or an array of strings can be set in an
      expression
  - field: options
    text: String of comma separated values or an array of strings can be set in an
      expression
  - field: options
    text: String of comma separated values or an array of strings can be set in an
      expression
  - field: options
    text: String of comma separated values or an array of strings can be set in an
      expression
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
  "$id": "https://n8n.io/schemas/nodes/serviceNow.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ServiceNow Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "upload",
        "delete",
        "get",
        "getAll",
        "create",
        "update"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "Authentication method to use",
          "type": "string",
          "enum": [
            "basicAuth",
            "oAuth2"
          ],
          "default": "oAuth2"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "attachment",
            "businessService",
            "configurationItems",
            "department",
            "dictionary",
            "incident",
            "tableRecord",
            "user",
            "userGroup",
            "userRole"
          ],
          "default": "user"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "getAll"
          ],
          "default": "getAll"
        },
        "tableName": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "id": {
          "description": "Unique identifier of the user",
          "type": "string",
          "default": ""
        },
        "inputDataFieldName": {
          "description": "Name of the binary property that contains the data to upload",
          "type": "string",
          "default": "data"
        },
        "options": {
          "description": "Whether to exclude Table API links for reference fields",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "attachmentId": {
          "description": "Sys_id value of the attachment to delete",
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
          "default": 50
        },
        "download": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "outputField": {
          "description": "Field name where downloaded data will be placed",
          "type": "string",
          "default": "data"
        },
        "short_description": {
          "description": "Short description of the user",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Whether to activate the user",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "updateFields": {
          "description": "Whether to activate the user",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "dataToSend": {
          "description": "Use when node input names match destination field names",
          "type": "string",
          "enum": [
            "mapInput",
            "columns",
            "nothing"
          ],
          "default": "columns"
        },
        "inputsToIgnore": {
          "description": "List of input properties to avoid sending, separated by commas. Leave empty to send all inputs.",
          "type": "string",
          "default": ""
        },
        "fieldsToSend": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add field to send"
          ]
        },
        "getOption": {
          "description": "Unique identifier of the user",
          "type": "string",
          "enum": [
            "id",
            "user_name"
          ],
          "default": "id"
        },
        "user_name": {
          "description": "Unique identifier of the user",
          "type": "string",
          "default": ""
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
      "name": "serviceNowOAuth2Api",
      "required": true
    },
    {
      "name": "serviceNowBasicApi",
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
