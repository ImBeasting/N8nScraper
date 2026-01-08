---
title: "Node: Freshworks CRM"
slug: "node-freshworkscrm"
version: "1"
updated: "2026-01-08"
summary: "Consume the Freshworks CRM API"
node_type: "regular"
group: "['transform']"
---

# Node: Freshworks CRM

**Purpose.** Consume the Freshworks CRM API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:freshworksCrm.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **freshworksCrmApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `freshworksCrmApi` | ✓ | - |

---

## Operations

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a task |
| Delete | `delete` | Delete a task |
| Get | `get` | Retrieve a task |
| Get Many | `getAll` | Retrieve many tasks |
| Update | `update` | Update a task |

### Account Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an account |
| Delete | `delete` | Delete an account |
| Get | `get` | Retrieve an account |
| Get Many | `getAll` | Retrieve many accounts |
| Update | `update` | Update an account |

### Appointment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an appointment |
| Delete | `delete` | Delete an appointment |
| Get | `get` | Retrieve an appointment |
| Get Many | `getAll` | Retrieve many appointments |
| Update | `update` | Update an appointment |

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a contact |
| Delete | `delete` | Delete a contact |
| Get | `get` | Retrieve a contact |
| Get Many | `getAll` | Retrieve many contacts |
| Update | `update` | Update a contact |

### Deal Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a deal |
| Delete | `delete` | Delete a deal |
| Get | `get` | Retrieve a deal |
| Get Many | `getAll` | Retrieve many deals |
| Update | `update` | Update a deal |

### Note Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a note |
| Delete | `delete` | Delete a note |
| Update | `update` | Update a note |

### Salesactivity Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a sales activity |
| Delete | `delete` | Delete a sales activity |
| Get | `get` | Retrieve a sales activity |
| Get Many | `getAll` | Retrieve many sales activities |
| Update | `update` | Update a sales activity |

### Search Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Query | `query` | Search for records by entering search queries of your choice |
| Lookup | `lookup` | Search for the name or email address of records |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | account | ✗ | Resource to operate on |  |

**Resource options:**

* **Account** (`account`)
* **Appointment** (`appointment`)
* **Contact** (`contact`)
* **Deal** (`deal`)
* **Note** (`note`)
* **Sales Activity** (`salesActivity`)
* **Search** (`search`)
* **Task** (`task`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a task |  |

**Operation options:**

* **Create** (`create`) - Create a task
* **Delete** (`delete`) - Delete a task
* **Get** (`get`) - Retrieve a task
* **Get Many** (`getAll`) - Retrieve many tasks
* **Update** (`update`) - Update a task

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Title | `title` | string |  | ✓ | Title of the task |  |
| Due Date | `dueDate` | dateTime |  | ✓ | Timestamp that denotes when the task is due to be completed |  |
| Owner Name or ID | `ownerId` | options |  | ✓ | ID of the user to whom the task is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Target Type | `targetableType` | options | Contact | ✓ | Type of the entity for which the task is updated |  |

**Target Type options:**

* **Contact** (`Contact`)
* **Deal** (`Deal`)
* **SalesAccount** (`SalesAccount`)

| Target ID | `targetable_id` | string |  | ✓ | ID of the entity for which the task is created. The type of entity is selected in "Target Type". |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the user who created the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Creator Name or ID | `creater_id` | options |  | ID of the user who created the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Outcome Name or ID | `outcome_id` | options |  | ID of the outcome of the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Task Type ID | `task_type_id` | string |  | ID of the type of task |

</details>

| Name | `name` | string |  | ✓ | Name of the account |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Address of the account | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `address` | string |  | Address of the account |
| Annual Revenue | `annual_revenue` | number | 0 | Annual revenue of the account |
| Business Type Name or ID | `business_type_id` | options |  | ID of the business that the account belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| City | `city` | string |  | City that the account belongs to |
| Country | `country` | string |  | Country that the account belongs to |
| Facebook | `facebook` | string |  | Facebook username of the account |
| Industry Type Name or ID | `industry_type_id` | options |  | ID of the industry that the account belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| LinkedIn | `linkedin` | string |  | LinkedIn account of the account |
| Number of Employees | `number_of_employees` | number | 0 | Number of employees in the account |
| Owner Name or ID | `owner_id` | options |  | ID of the user to whom the account is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Parent Sales Account ID | `parent_sales_account_id` | string |  | Parent account ID of the account |
| Phone | `phone` | string |  | Phone number of the account |
| State | `state` | string |  | State that the account belongs to |
| Territory Name or ID | `territory_id` | options |  | ID of the territory that the account belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Twitter | `twitter` | string |  | Twitter username of the account |
| Website | `website` | string |  | Website of the account |
| Zipcode | `zipcode` | string |  | Zipcode of the region that the account belongs to |

</details>

| Title | `title` | string |  | ✓ | Title of the appointment |  |
| Start Date | `fromDate` | dateTime |  | ✓ | Timestamp that denotes the start of appointment. Start date if this is an all-day appointment. |  |
| End Date | `endDate` | dateTime |  | ✓ | Timestamp that denotes the end of appointment. End date if this is an all-day appointment. |  |
| Attendees | `attendees` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Attendee |  |

<details>
<summary><strong>Attendees sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attendee | `attendee` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the user who created the appointment. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Creator Name or ID | `creater_id` | options |  | ID of the user who created the appointment. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Is All-Day | `is_allday` | boolean | False | Whether it is an all-day appointment or not |
| Latitude | `latitude` | string |  | Latitude of the location when you check in for an appointment |
| Location | `location` | string |  | Location of the appointment |
| Longitude | `longitude` | string |  | Longitude of the location when you check in for an appointment |
| Outcome Name or ID | `outcome_id` | options |  | ID of outcome of Appointment sales activity type. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Target ID | `targetable_id` | string |  | ID of contact/account against whom appointment is created |
| Target Type | `targetable_type` | options | Contact |  |
| Time Zone | `time_zone` | options |  | Timezone that the appointment is scheduled in |

</details>

| First Name | `firstName` | string |  | ✓ | First name of the contact |  |
| Last Name | `lastName` | string |  | ✓ | Last name of the contact |  |
| Email Address | `emails` | string |  | ✓ | Email addresses of the contact | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Address of the contact | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `address` | string |  | Address of the contact |
| Campaign Name or ID | `campaign_id` | options |  | ID of the campaign that led your contact to your webapp. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| City | `city` | string |  | City that the contact belongs to |
| Contact Status Name or ID | `contact_status_id` | options |  | ID of the contact status that the contact belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Country | `country` | string |  | Country that the contact belongs to |
| External ID | `external_id` | string |  | External ID of the contact |
| Facebook | `facebook` | string |  | Facebook username of the contact |
| Job Title | `job_title` | string |  | Designation of the contact in the account they belong to |
| Keywords | `keyword` | string |  | Keywords that the contact used to reach your website/web app |
| Lead Source ID | `lead_source_id` | string |  | ID of the source where contact came from |
| Lifecycle Stage Name or ID | `lifecycle_stage_id` | options |  | ID of the lifecycle stage that the contact belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| LinkedIn | `linkedin` | string |  | LinkedIn account of the contact |
| Medium | `medium` | string |  | Medium that led your contact to your website/webapp |
| Mobile Number | `mobile_number` | string |  | Mobile phone number of the contact |
| Owner Name or ID | `owner_id` | options |  | ID of the user to whom the contact is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Sales Account Names or IDs | `sales_accounts` | multiOptions | [] | Accounts which contact belongs to. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| State | `state` | string |  | State that the contact belongs to |
| Subscription Status | `subscription_status` | string |  | Status of subscription that the contact is in |
| Subscription Types | `subscription_types` | string |  | Type of subscription that the contact is in |
| Territory Name or ID | `territory_id` | options |  | ID of the territory that the contact belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Time Zone | `time_zone` | string |  | Timezone that the contact belongs to |
| Twitter | `twitter` | string |  | Twitter username of the contact |
| Work Number | `work_number` | string |  | Work phone number of the contact |
| Zipcode | `zipcode` | string |  | Zipcode of the region that the contact belongs to |

</details>

| Amount | `amount` | number | 0 | ✓ | Value of the deal |  |
| Name | `name` | string |  | ✓ | Name of the deal |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Value of the deal in base currency | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Base Currency Amount | `base_currency_amount` | number | 0 | Value of the deal in base currency |
| Campaign Name or ID | `campaign_id` | options |  | ID of the campaign that landed this deal. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Currency Name or ID | `currency_id` | options |  | ID of the currency that the deal belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Deal Payment Status Name or ID | `deal_payment_status_id` | options |  | ID of the mode of payment for the deal. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Deal Pipeline Name or ID | `deal_pipeline_id` | options |  | ID of the deal pipeline that it belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Deal Product Name or ID | `deal_product_id` | options |  | ID of the product that the deal belongs to (in a multi-product company). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Deal Reason Name or ID | `deal_reason_id` | options |  | ID of the reason for losing the deal. Can only be set if the deal is in 'Lost' stage. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Deal Stage Name or ID | `deal_stage_id` | options |  | ID of the deal stage that the deal belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Deal Type Name or ID | `deal_type_id` | options |  | ID of the deal type that the deal belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Lead Source ID | `lead_source_id` | string |  | ID of the source where deal came from |
| Owner Name or ID | `owner_id` | options |  | ID of the user to whom the deal is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Probability | `probability` | number | 0 | Probability of winning the deal as a number between 0 and 100 |
| Sales Account Name or ID | `sales_account_id` | options |  | ID of the account that the deal belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Territory Name or ID | `territory_id` | options |  | ID of the territory that the deal belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Content | `description` | string |  | ✓ | Content of the note |  |
| Target Type | `targetableType` | options | Contact | ✓ | Type of the entity for which the note is created |  |

**Target Type options:**

* **Contact** (`Contact`)
* **Deal** (`Deal`)
* **Sales Account** (`SalesAccount`)

| Target ID | `targetable_id` | string |  | ✓ | ID of the entity for which note is created. The type of entity is selected in "Target Type". |  |
| Sales Activity Type Name or ID | `sales_activity_type_id` | options |  | ✗ | ID of a sales activity type for which the sales activity is created. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Title | `title` | string |  | ✓ | Title of the sales activity to create |  |
| Owner Name or ID | `ownerId` | options |  | ✓ | ID of the user who owns the sales activity. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Start Date | `from_date` | dateTime |  | ✓ | Timestamp that denotes the end of sales activity |  |
| End Date | `end_date` | dateTime |  | ✓ | Timestamp that denotes the end of sales activity |  |
| Target Type | `targetableType` | options | Contact | ✓ | Type of the entity for which the sales activity is created |  |

**Target Type options:**

* **Contact** (`Contact`)
* **Deal** (`Deal`)
* **Sales Account** (`SalesAccount`)

| Target ID | `targetable_id` | string |  | ✓ | ID of the entity for which the sales activity is created. The type of entity is selected in "Target Type". |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the user who created the sales activity. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Creator Name or ID | `creater_id` | options |  | ID of the user who created the sales activity. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Latitude | `latitude` | string |  | Latitude of the location when you check in on a sales activity |
| Location | `location` | string |  | Location of the sales activity |
| Longitude | `longitude` | string |  | Longitude of the location when you check in for a sales activity |
| Notes | `notes` | string |  | Description about the sales activity |
| Sales Activity Outcome Name or ID | `sales_activity_outcome_id` | options |  | ID of a sales activity's outcome. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ | ID of the task to delete |  |
| Account ID | `accountId` | string |  | ✓ | ID of the account to delete |  |
| Appointment ID | `appointmentId` | string |  | ✓ | ID of the appointment to delete |  |
| Contact ID | `contactId` | string |  | ✓ | ID of the contact to delete |  |
| Deal ID | `dealId` | string |  | ✓ | ID of the deal to delete |  |
| Note ID | `noteId` | string |  | ✓ | ID of the note to delete |  |
| Sales Activity ID | `salesActivityId` | string |  | ✓ | ID of the salesActivity to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ | ID of the task to retrieve |  |
| Account ID | `accountId` | string |  | ✓ | ID of the account to retrieve |  |
| Appointment ID | `appointmentId` | string |  | ✓ | ID of the appointment to retrieve |  |
| Contact ID | `contactId` | string |  | ✓ | ID of the contact to retrieve |  |
| Deal ID | `dealId` | string |  | ✓ | ID of the deal to retrieve |  |
| Sales Activity ID | `salesActivityId` | string |  | ✓ | ID of the salesActivity to retrieve |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include | `include` | options | owner |  |
| Status | `filter` | options | open |  |

</details>

| View Name or ID | `view` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Filters | `filters` | collection | {} | ✗ | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include | `include` | options | creater |  |
| Time | `filter` | options | upcoming |  |

</details>

| View Name or ID | `view` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| View Name or ID | `view` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:∞ |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Task ID | `taskId` | string |  | ✓ | ID of the task to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the user who created the sales activity. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Creator Name or ID | `creater_id` | options |  | ID of the user who created the sales activity. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Due Date | `dueDate` | dateTime |  | Timestamp that denotes when the task is due to be completed |
| Outcome Name or ID | `outcome_id` | options |  | ID of the outcome of the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Owner Name or ID | `owner_id` | options |  | ID of the user to whom the task is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Target ID | `targetable_id` | string |  | ID of the entity for which the task is updated. The type of entity is selected in "Target Type". |
| Target Type | `targetable_type` | options | Contact | Type of the entity for which the task is updated |
| Task Type ID | `task_type_id` | string |  | ID of the type of task |
| Title | `title` | string |  | Title of the task |

</details>

| Account ID | `accountId` | string |  | ✓ | ID of the account to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Address of the account | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `address` | string |  | Address of the account |
| Annual Revenue | `annual_revenue` | number | 0 | Annual revenue of the account |
| Business Type Name or ID | `business_type_id` | options |  | ID of the business that the account belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| City | `city` | string |  | City that the account belongs to |
| Country | `country` | string |  | Country that the account belongs to |
| Facebook | `facebook` | string |  | Facebook username of the account |
| Industry Type Name or ID | `industry_type_id` | options |  | ID of the industry that the account belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| LinkedIn | `linkedin` | string |  | LinkedIn account of the account |
| Name | `name` | string |  | Name of the account |
| Number of Employees | `number_of_employees` | number | 0 | Number of employees in the account |
| Owner Name or ID | `owner_id` | options |  | ID of the user to whom the account is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Parent Sales Account ID | `parent_sales_account_id` | string |  | Parent account ID of the account |
| Phone | `phone` | string |  | Phone number of the account |
| State | `state` | string |  | State that the account belongs to |
| Territory Name or ID | `territory_id` | options |  | ID of the territory that the account belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Twitter | `twitter` | string |  | Twitter username of the account |
| Website | `website` | string |  | Website of the account |
| Zipcode | `zipcode` | string |  | Zipcode of the region that the account belongs to |

</details>

| Appointment ID | `appointmentId` | string |  | ✓ | ID of the appointment to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attendees | `attendees` | fixedCollection | {} | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Creator Name or ID | `creater_id` | options | [] | ID of the user who created the appointment. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| End Date | `endDate` | dateTime |  | Timestamp that denotes the end of appointment. End date if this is an all-day appointment. |
| Is All-Day | `is_allday` | boolean | False | Whether it is an all-day appointment or not |
| Latitude | `latitude` | string |  | Latitude of the location when you check in for an appointment |
| Location | `location` | string |  | Location of the appointment |
| Longitude | `longitude` | string |  | Longitude of the location when you check in for an appointment |
| Outcome Name or ID | `outcome_id` | options |  | ID of outcome of Appointment sales activity type. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Start Date | `fromDate` | dateTime |  | Timestamp that denotes the start of appointment. Start date if this is an all-day appointment. |
| Target ID | `targetable_id` | string |  | ID of contact/account against whom appointment is created |
| Target Type | `targetable_type` | options | Contact |  |
| Time Zone | `time_zone` | options |  | Timezone that the appointment is scheduled in |
| Title | `title` | string |  | Title of the appointment |

</details>

| Contact ID | `contactId` | string |  | ✓ | ID of the contact to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Address of the contact | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `address` | string |  | Address of the contact |
| Campaign Name or ID | `campaign_id` | options |  | ID of the campaign that led your contact to your webapp. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| City | `city` | string |  | City that the contact belongs to |
| Contact Status Name or ID | `contact_status_id` | options |  | ID of the contact status that the contact belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Country | `country` | string |  | Country that the contact belongs to |
| External ID | `external_id` | string |  | External ID of the contact |
| Facebook | `facebook` | string |  | Facebook username of the contact |
| First Name | `first_name` | string |  | First name of the contact |
| Job Title | `job_title` | string |  | Designation of the contact in the account they belong to |
| Keywords | `keyword` | string |  | Keywords that the contact used to reach your website/web app |
| Last Name | `last_name` | string |  | Last name of the contact |
| Lead Source Name or ID | `lead_source_id` | options |  | ID of the source where contact came from. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Lifecycle Stage Name or ID | `lifecycle_stage_id` | options |  | ID of the lifecycle stage that the contact belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| LinkedIn | `linkedin` | string |  | LinkedIn account of the contact |
| Medium | `medium` | string |  | Medium that led your contact to your website/webapp |
| Mobile Number | `mobile_number` | string |  | Mobile phone number of the contact |
| Owner Name or ID | `owner_id` | options |  | ID of the user to whom the contact is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Sales Account Names or IDs | `sales_accounts` | multiOptions | [] | Accounts which contact belongs to. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| State | `state` | string |  | State that the contact belongs to |
| Subscription Status Name or ID | `subscription_status` | options |  | Status of subscription that the contact is in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Subscription Types Name or ID | `subscription_types` | options |  | Type of subscription that the contact is in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Territory Name or ID | `territory_id` | options |  | ID of the territory that the contact belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Time Zone | `time_zone` | string |  | Timezone that the contact belongs to |
| Twitter | `twitter` | string |  | Twitter username of the contact |
| Work Number | `work_number` | string |  | Work phone number of the contact |
| Zipcode | `zipcode` | string |  | Zipcode of the region that the contact belongs to |

</details>

| Deal ID | `dealId` | string |  | ✓ | ID of the deal to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Value of the deal | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Amount | `amount` | number | 0 | Value of the deal |
| Base Currency Amount | `base_currency_amount` | number | 0 | Value of the deal in base currency |
| Campaign Name or ID | `campaign_id` | options |  | ID of the campaign that landed this deal. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Currency Name or ID | `currency_id` | options |  | ID of the currency that the deal belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Deal Payment Status Name or ID | `deal_payment_status_id` | options |  | ID of the mode of payment for the deal. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Deal Pipeline Name or ID | `deal_pipeline_id` | options |  | ID of the deal pipeline that it belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Deal Product Name or ID | `deal_product_id` | options |  | ID of the product that the deal belongs to (in a multi-product company). Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Deal Reason Name or ID | `deal_reason_id` | options |  | ID of the reason for losing the deal. Can only be set if the deal is in 'Lost' stage. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Deal Stage Name or ID | `deal_stage_id` | options |  | ID of the deal stage that the deal belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Deal Type Name or ID | `deal_type_id` | options |  | ID of the deal type that the deal belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Lead Source ID | `lead_source_id` | string |  | ID of the source where deal came from |
| Name | `name` | string |  | Name of the deal |
| Owner Name or ID | `owner_id` | options |  | ID of the user to whom the deal is assigned. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Probability | `probability` | number | 0 | Probability of winning the deal as a number between 0 and 100 |
| Sales Account Name or ID | `sales_account_id` | options |  | ID of the account that the deal belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Territory Name or ID | `territory_id` | options |  | ID of the territory that the deal belongs to. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Note ID | `noteId` | string |  | ✓ | ID of the note to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Content of the note | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Content | `description` | string |  | Content of the note |
| Target ID | `targetable_id` | string |  | ID of the entity for which the note is updated |
| Target Type | `targetable_type` | options | Contact | Type of the entity for which the note is updated |

</details>

| Sales Activity ID | `salesActivityId` | string |  | ✓ | ID of the salesActivity to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the user who created the sales activity. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Creator Name or ID | `creater_id` | options |  | ID of the user who created the sales activity. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Start Date | `end_date` | dateTime |  | Timestamp that denotes the start of the sales activity |
| Latitude | `latitude` | string |  | Latitude of the location when you check in on a sales activity |
| Location | `location` | string |  | Location of the sales activity |
| Longitude | `longitude` | string |  | Longitude of the location when you check in for a sales activity |
| Notes | `notes` | string |  | Description about the sales activity |
| Owner Name or ID | `owner_id` | options |  | ID of the user who owns the sales activity. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Sales Activity Outcome Name or ID | `sales_activity_outcome_id` | options |  | ID of a sales activity's outcome. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Sales Activity Type Name or ID | `sales_activity_type_id` | options |  | ID of a sales activity type for which the sales activity is updated. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Start Date | `from_date` | dateTime |  | Timestamp that denotes the start of the sales activity |
| Target ID | `targetable_id` | string |  | ID of the entity for which the sales activity is updated. The type of entity is selected in "Target Type". |
| Target Type | `targetable_type` | options | Contact | Type of the entity for which the sales activity is updated |
| Title | `title` | string |  | Title of the sales activity to update |

</details>


### Query parameters (`query`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Search Term | `query` | string |  | ✓ | Enter a term that will be used for searching entities |  |
| Search on Entities | `entities` | multiOptions | [] | ✓ | Enter a term that will be used for searching entities |  |

**Search on Entities options:**

* **Contact** (`contact`)
* **Deal** (`deal`)
* **Sales Account** (`sales_account`)
* **User** (`user`)

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 25 | ✗ | Max number of results to return | min:1, max:∞ |

### Lookup parameters (`lookup`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Search Field | `searchField` | options |  | ✓ | Only allowed custom fields of type "Text field", "Number", "Dropdown" or "Radio button" |  |

**Search Field options:**

* **Email** (`email`)
* **Name** (`name`)
* **Custom Field** (`customField`) - Only allowed custom fields of type "Text field", "Number", "Dropdown" or "Radio button"

| Custom Field Name | `customFieldName` | string |  | ✓ |  |  |
| Custom Field Value | `customFieldValue` | string |  | ✓ |  |  |
| Field Value | `fieldValue` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | Use 'entities' to query against related entities. You can include multiple entities at once, provided the field is available in both entities or else you'd receive an error response. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Entities | `entities` | multiOptions | [] | Use 'entities' to query against related entities. You can include multiple entities at once, provided the field is available in both entities or else you'd receive an error response. |

</details>


---

## Load Options Methods

- `getAccounts`

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
* Categories: Marketing, Sales
* Aliases: Freshdesk

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: freshworksCrm
displayName: Freshworks CRM
description: Consume the Freshworks CRM API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: freshworksCrmApi
  required: true
operations:
- id: create
  name: Create
  description: Create a task
  params:
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the task
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - salesActivity
          operation:
          - create
    typeInfo: &id002
      type: string
      displayName: Title
      name: title
  - id: dueDate
    name: Due Date
    type: dateTime
    default: ''
    required: true
    description: Timestamp that denotes when the task is due to be completed
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - create
    typeInfo:
      type: dateTime
      displayName: Due Date
      name: dueDate
  - id: ownerId
    name: Owner Name or ID
    type: options
    default: ''
    required: true
    description: ID of the user to whom the task is assigned. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - salesActivity
          operation:
          - create
    typeInfo: &id010
      type: options
      displayName: Owner Name or ID
      name: ownerId
      typeOptions:
        loadOptionsMethod: getUsers
      possibleValues: []
  - id: targetableType
    name: Target Type
    type: options
    default: Contact
    required: true
    description: Type of the entity for which the task is updated
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - salesActivity
          operation:
          - create
    typeInfo: &id006
      type: options
      displayName: Target Type
      name: targetableType
      possibleValues:
      - value: Contact
        name: Contact
        description: ''
      - value: Deal
        name: Deal
        description: ''
      - value: SalesAccount
        name: Sales Account
        description: ''
  - id: targetable_id
    name: Target ID
    type: string
    default: ''
    required: true
    description: ID of the entity for which the task is created. The type of entity
      is selected in "Target Type".
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - salesActivity
          operation:
          - create
    typeInfo: &id008
      type: string
      displayName: Target ID
      name: targetable_id
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the account
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - create
    typeInfo: &id004
      type: string
      displayName: Name
      name: name
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the appointment
    validation: *id001
    typeInfo: *id002
  - id: fromDate
    name: Start Date
    type: dateTime
    default: ''
    required: true
    description: Timestamp that denotes the start of appointment. Start date if this
      is an all-day appointment.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - appointment
          operation:
          - create
    typeInfo:
      type: dateTime
      displayName: Start Date
      name: fromDate
  - id: endDate
    name: End Date
    type: dateTime
    default: ''
    required: true
    description: Timestamp that denotes the end of appointment. End date if this is
      an all-day appointment.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - appointment
          operation:
          - create
    typeInfo:
      type: dateTime
      displayName: End Date
      name: endDate
  - id: attendees
    name: Attendees
    type: fixedCollection
    default: {}
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Attendee
    validation:
      displayOptions:
        show:
          resource:
          - appointment
          operation:
          - create
    typeInfo:
      type: fixedCollection
      displayName: Attendees
      name: attendees
      typeOptions:
        multipleValues: true
      subProperties:
      - name: attendee
        displayName: Attendee
        values:
        - displayName: Type
          name: type
          type: options
          value: contact
          default: contact
          options:
          - name: Contact
            value: contact
            displayName: Contact
          - name: User
            value: user
            displayName: User
        - displayName: User Name or ID
          name: userId
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getUsers
          displayOptions:
            show:
              type:
              - user
        - displayName: Contact ID
          name: contactId
          type: string
          default: ''
          displayOptions:
            show:
              type:
              - contact
  - id: firstName
    name: First Name
    type: string
    default: ''
    required: true
    description: First name of the contact
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - create
    typeInfo:
      type: string
      displayName: First Name
      name: firstName
  - id: lastName
    name: Last Name
    type: string
    default: ''
    required: true
    description: Last name of the contact
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - create
    typeInfo:
      type: string
      displayName: Last Name
      name: lastName
  - id: emails
    name: Email Address
    type: string
    default: ''
    required: true
    description: Email addresses of the contact
    validation:
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - create
    typeInfo:
      type: string
      displayName: Email Address
      name: emails
  - id: amount
    name: Amount
    type: number
    default: 0
    required: true
    description: Value of the deal
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - create
    typeInfo:
      type: number
      displayName: Amount
      name: amount
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the deal
    validation: *id003
    typeInfo: *id004
  - id: description
    name: Content
    type: string
    default: ''
    required: true
    description: Content of the note
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - note
          operation:
          - create
    typeInfo:
      type: string
      displayName: Content
      name: description
      typeOptions:
        rows: 5
  - id: targetableType
    name: Target Type
    type: options
    default: Contact
    required: true
    description: Type of the entity for which the note is created
    validation: *id005
    typeInfo: *id006
  - id: targetable_id
    name: Target ID
    type: string
    default: ''
    required: true
    description: ID of the entity for which note is created. The type of entity is
      selected in "Target Type".
    validation: *id007
    typeInfo: *id008
  - id: sales_activity_type_id
    name: Sales Activity Type Name or ID
    type: options
    default: ''
    required: false
    description: ID of a sales activity type for which the sales activity is created.
      Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      displayOptions:
        show:
          resource:
          - salesActivity
          operation:
          - create
    typeInfo:
      type: options
      displayName: Sales Activity Type Name or ID
      name: sales_activity_type_id
      typeOptions:
        loadOptionsMethod: getSalesActivityTypes
      possibleValues: []
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the sales activity to create
    validation: *id001
    typeInfo: *id002
  - id: ownerId
    name: Owner Name or ID
    type: options
    default: ''
    required: true
    description: ID of the user who owns the sales activity. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id009
    typeInfo: *id010
  - id: from_date
    name: Start Date
    type: dateTime
    default: ''
    required: true
    description: Timestamp that denotes the end of sales activity
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - salesActivity
          operation:
          - create
    typeInfo:
      type: dateTime
      displayName: Start Date
      name: from_date
  - id: end_date
    name: End Date
    type: dateTime
    default: ''
    required: true
    description: Timestamp that denotes the end of sales activity
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - salesActivity
          operation:
          - create
    typeInfo:
      type: dateTime
      displayName: End Date
      name: end_date
  - id: targetableType
    name: Target Type
    type: options
    default: Contact
    required: true
    description: Type of the entity for which the sales activity is created
    validation: *id005
    typeInfo: *id006
  - id: targetable_id
    name: Target ID
    type: string
    default: ''
    required: true
    description: ID of the entity for which the sales activity is created. The type
      of entity is selected in "Target Type".
    validation: *id007
    typeInfo: *id008
- id: delete
  name: Delete
  description: Delete a task
  params:
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of the task to delete
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - update
    typeInfo: &id012
      type: string
      displayName: Task ID
      name: taskId
  - id: accountId
    name: Account ID
    type: string
    default: ''
    required: true
    description: ID of the account to delete
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - account
          operation:
          - update
    typeInfo: &id014
      type: string
      displayName: Account ID
      name: accountId
  - id: appointmentId
    name: Appointment ID
    type: string
    default: ''
    required: true
    description: ID of the appointment to delete
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - appointment
          operation:
          - update
    typeInfo: &id016
      type: string
      displayName: Appointment ID
      name: appointmentId
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact to delete
    validation: &id017
      required: true
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - update
    typeInfo: &id018
      type: string
      displayName: Contact ID
      name: contactId
  - id: dealId
    name: Deal ID
    type: string
    default: ''
    required: true
    description: ID of the deal to delete
    validation: &id019
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - update
    typeInfo: &id020
      type: string
      displayName: Deal ID
      name: dealId
  - id: noteId
    name: Note ID
    type: string
    default: ''
    required: true
    description: ID of the note to delete
    validation: &id029
      required: true
      displayOptions:
        show:
          resource:
          - note
          operation:
          - update
    typeInfo: &id030
      type: string
      displayName: Note ID
      name: noteId
  - id: salesActivityId
    name: Sales Activity ID
    type: string
    default: ''
    required: true
    description: ID of the salesActivity to delete
    validation: &id021
      required: true
      displayOptions:
        show:
          resource:
          - salesActivity
          operation:
          - update
    typeInfo: &id022
      type: string
      displayName: Sales Activity ID
      name: salesActivityId
- id: get
  name: Get
  description: Retrieve a task
  params:
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of the task to retrieve
    validation: *id011
    typeInfo: *id012
  - id: accountId
    name: Account ID
    type: string
    default: ''
    required: true
    description: ID of the account to retrieve
    validation: *id013
    typeInfo: *id014
  - id: appointmentId
    name: Appointment ID
    type: string
    default: ''
    required: true
    description: ID of the appointment to retrieve
    validation: *id015
    typeInfo: *id016
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact to retrieve
    validation: *id017
    typeInfo: *id018
  - id: dealId
    name: Deal ID
    type: string
    default: ''
    required: true
    description: ID of the deal to retrieve
    validation: *id019
    typeInfo: *id020
  - id: salesActivityId
    name: Sales Activity ID
    type: string
    default: ''
    required: true
    description: ID of the salesActivity to retrieve
    validation: *id021
    typeInfo: *id022
- id: getAll
  name: Get Many
  description: Retrieve many tasks
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id023
      displayOptions:
        show:
          resource:
          - search
          operation:
          - query
    typeInfo: &id024
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id025
      displayOptions:
        show:
          resource:
          - search
          operation:
          - query
          returnAll:
          - false
    typeInfo: &id026
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
  - id: view
    name: View Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id027
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - getAll
    typeInfo: &id028
      type: options
      displayName: View Name or ID
      name: view
      typeOptions:
        loadOptionsMethod: getDealViews
      possibleValues: []
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id023
    typeInfo: *id024
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id025
    typeInfo: *id026
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id023
    typeInfo: *id024
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id025
    typeInfo: *id026
  - id: view
    name: View Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id027
    typeInfo: *id028
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id023
    typeInfo: *id024
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id025
    typeInfo: *id026
  - id: view
    name: View Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id027
    typeInfo: *id028
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id023
    typeInfo: *id024
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id025
    typeInfo: *id026
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id023
    typeInfo: *id024
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id025
    typeInfo: *id026
- id: update
  name: Update
  description: Update a task
  params:
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of the task to update
    validation: *id011
    typeInfo: *id012
  - id: accountId
    name: Account ID
    type: string
    default: ''
    required: true
    description: ID of the account to update
    validation: *id013
    typeInfo: *id014
  - id: appointmentId
    name: Appointment ID
    type: string
    default: ''
    required: true
    description: ID of the appointment to update
    validation: *id015
    typeInfo: *id016
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact to update
    validation: *id017
    typeInfo: *id018
  - id: dealId
    name: Deal ID
    type: string
    default: ''
    required: true
    description: ID of the deal to update
    validation: *id019
    typeInfo: *id020
  - id: noteId
    name: Note ID
    type: string
    default: ''
    required: true
    description: ID of the note to update
    validation: *id029
    typeInfo: *id030
  - id: salesActivityId
    name: Sales Activity ID
    type: string
    default: ''
    required: true
    description: ID of the salesActivity to update
    validation: *id021
    typeInfo: *id022
- id: query
  name: Query
  description: Search for records by entering search queries of your choice
  params:
  - id: query
    name: Search Term
    type: string
    default: ''
    required: true
    description: Enter a term that will be used for searching entities
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - search
          operation:
          - query
    typeInfo:
      type: string
      displayName: Search Term
      name: query
  - id: entities
    name: Search on Entities
    type: multiOptions
    default: []
    required: true
    description: Enter a term that will be used for searching entities
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - search
          operation:
          - query
    typeInfo:
      type: multiOptions
      displayName: Search on Entities
      name: entities
      possibleValues:
      - value: contact
        name: Contact
        description: ''
      - value: deal
        name: Deal
        description: ''
      - value: sales_account
        name: Sales Account
        description: ''
      - value: user
        name: User
        description: ''
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id023
    typeInfo: *id024
  - id: limit
    name: Limit
    type: number
    default: 25
    required: false
    description: Max number of results to return
    validation: *id025
    typeInfo: *id026
- id: lookup
  name: Lookup
  description: Search for the name or email address of records
  params:
  - id: searchField
    name: Search Field
    type: options
    default: ''
    required: true
    description: Only allowed custom fields of type "Text field", "Number", "Dropdown"
      or "Radio button"
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - search
          operation:
          - lookup
    typeInfo:
      type: options
      displayName: Search Field
      name: searchField
      possibleValues:
      - value: email
        name: Email
        description: ''
      - value: name
        name: Name
        description: ''
      - value: customField
        name: Custom Field
        description: Only allowed custom fields of type "Text field", "Number", "Dropdown"
          or "Radio button"
  - id: customFieldName
    name: Custom Field Name
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - search
          operation:
          - lookup
          searchField:
          - customField
    typeInfo:
      type: string
      displayName: Custom Field Name
      name: customFieldName
  - id: customFieldValue
    name: Custom Field Value
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - search
          operation:
          - lookup
          searchField:
          - customField
    typeInfo:
      type: string
      displayName: Custom Field Value
      name: customFieldValue
  - id: fieldValue
    name: Field Value
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - search
          operation:
          - lookup
          searchField:
          - email
          - name
    typeInfo:
      type: string
      displayName: Field Value
      name: fieldValue
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
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: attendees
    text: Add Attendee
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
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
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/freshworksCrm.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Freshworks CRM Node",
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
        "query",
        "lookup"
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
            "account",
            "appointment",
            "contact",
            "deal",
            "note",
            "salesActivity",
            "search",
            "task"
          ],
          "default": "account"
        },
        "operation": {
          "description": "Search for records by entering search queries of your choice",
          "type": "string",
          "enum": [
            "query",
            "lookup"
          ],
          "default": "query"
        },
        "title": {
          "description": "Title of the sales activity to create",
          "type": "string",
          "default": ""
        },
        "dueDate": {
          "description": "Timestamp that denotes when the task is due to be completed",
          "type": "string",
          "default": ""
        },
        "ownerId": {
          "description": "ID of the user who owns the sales activity. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "targetableType": {
          "description": "Type of the entity for which the sales activity is created",
          "type": "string",
          "enum": [
            "Contact",
            "Deal",
            "SalesAccount"
          ],
          "default": "Contact"
        },
        "targetable_id": {
          "description": "ID of the entity for which the sales activity is created. The type of entity is selected in \"Target Type\".",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "ID of the user who created the sales activity. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "taskId": {
          "description": "ID of the task to update",
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
          "default": 25
        },
        "filters": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "updateFields": {
          "description": "ID of the user who created the sales activity. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "name": {
          "description": "Name of the deal",
          "type": "string",
          "default": ""
        },
        "accountId": {
          "description": "ID of the account to update",
          "type": "string",
          "default": ""
        },
        "view": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "fromDate": {
          "description": "Timestamp that denotes the start of appointment. Start date if this is an all-day appointment.",
          "type": "string",
          "default": ""
        },
        "endDate": {
          "description": "Timestamp that denotes the end of appointment. End date if this is an all-day appointment.",
          "type": "string",
          "default": ""
        },
        "attendees": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Attendee"
          ]
        },
        "appointmentId": {
          "description": "ID of the appointment to update",
          "type": "string",
          "default": ""
        },
        "firstName": {
          "description": "First name of the contact",
          "type": "string",
          "default": ""
        },
        "lastName": {
          "description": "Last name of the contact",
          "type": "string",
          "default": ""
        },
        "emails": {
          "description": "Email addresses of the contact",
          "type": "string",
          "default": "",
          "format": "email"
        },
        "contactId": {
          "description": "ID of the contact to update",
          "type": "string",
          "default": ""
        },
        "amount": {
          "description": "Value of the deal",
          "type": "number",
          "default": 0
        },
        "dealId": {
          "description": "ID of the deal to update",
          "type": "string",
          "default": ""
        },
        "description": {
          "description": "Content of the note",
          "type": "string",
          "default": ""
        },
        "noteId": {
          "description": "ID of the note to update",
          "type": "string",
          "default": ""
        },
        "sales_activity_type_id": {
          "description": "ID of a sales activity type for which the sales activity is created. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "from_date": {
          "description": "Timestamp that denotes the end of sales activity",
          "type": "string",
          "default": ""
        },
        "end_date": {
          "description": "Timestamp that denotes the end of sales activity",
          "type": "string",
          "default": ""
        },
        "salesActivityId": {
          "description": "ID of the salesActivity to update",
          "type": "string",
          "default": ""
        },
        "query": {
          "description": "Enter a term that will be used for searching entities",
          "type": "string",
          "default": ""
        },
        "entities": {
          "description": "Enter a term that will be used for searching entities",
          "type": "string",
          "default": []
        },
        "searchField": {
          "description": "Only allowed custom fields of type \"Text field\", \"Number\", \"Dropdown\" or \"Radio button\"",
          "type": "string",
          "enum": [
            "email",
            "name",
            "customField"
          ],
          "default": ""
        },
        "customFieldName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "customFieldValue": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "fieldValue": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "Use 'entities' to query against related entities. You can include multiple entities at once, provided the field is available in both entities or else you'd receive an error response.",
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
      "name": "freshworksCrmApi",
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
