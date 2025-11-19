---
title: "Node: Salesforce"
slug: "node-salesforce"
version: "1"
updated: "2025-11-13"
summary: "Consume Salesforce API"
node_type: "regular"
group: "['output']"
---

# Node: Salesforce

**Purpose.** Consume Salesforce API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:salesforce.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **salesforceOAuth2Api**: N/A
- **salesforceJwtApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `salesforceOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |
| `salesforceJwtApi` | ✓ | {'show': {'authentication': ['jwt']}} |

---

## API Patterns

**HTTP Methods:** POST

**Headers Used:** Content-Type

---

## Operations

### Lead Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Lead To Campaign | `addToCampaign` | Add lead to a campaign |
| Add Note | `addNote` | Add note to a lead |
| Create | `create` | Create a lead |
| Create or Update | `upsert` | Create a new lead, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a lead |
| Get | `get` | Get a lead |
| Get Many | `getAll` | Get many leads |
| Get Summary | `getSummary` | Returns an overview of Lead's metadata |
| Update | `update` | Update a lead |

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Contact To Campaign | `addToCampaign` | Add contact to a campaign |
| Add Note | `addNote` | Add note to a contact |
| Create | `create` | Create a contact |
| Create or Update | `upsert` | Create a new contact, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a contact |
| Get | `get` | Get a contact |
| Get Many | `getAll` | Get many contacts |
| Get Summary | `getSummary` | Returns an overview of contact's metadata |
| Update | `update` | Update a contact |

### Customobject Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a custom object record |
| Create or Update | `upsert` | Create a new record, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a custom object record |
| Get | `get` | Get a custom object record |
| Get Many | `getAll` | Get many custom object records |
| Update | `update` | Update a custom object record |

### Document Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Upload | `upload` | Upload a document |

### Opportunity Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Note | `addNote` | Add note to an opportunity |
| Create | `create` | Create an opportunity |
| Create or Update | `upsert` | Create a new opportunity, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete an opportunity |
| Get | `get` | Get an opportunity |
| Get Many | `getAll` | Get many opportunities |
| Get Summary | `getSummary` | Returns an overview of opportunity's metadata |
| Update | `update` | Update an opportunity |

### Account Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Note | `addNote` | Add note to an account |
| Create | `create` | Create an account |
| Create or Update | `upsert` | Create a new account, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete an account |
| Get | `get` | Get an account |
| Get Many | `getAll` | Get many accounts |
| Get Summary | `getSummary` | Returns an overview of account's metadata |
| Update | `update` | Update an account |

### Search Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Query | `query` | Execute a SOQL query that returns all the results in a single response |

### Case Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add Comment | `addComment` | Add a comment to a case |
| Create | `create` | Create a case |
| Delete | `delete` | Delete a case |
| Get | `get` | Get a case |
| Get Many | `getAll` | Get many cases |
| Get Summary | `getSummary` | Returns an overview of case's metadata |
| Update | `update` | Update a case |

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a task |
| Delete | `delete` | Delete a task |
| Get | `get` | Get a task |
| Get Many | `getAll` | Get many tasks |
| Get Summary | `getSummary` | Returns an overview of task's metadata |
| Update | `update` | Update a task |

### Attachment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a attachment |
| Delete | `delete` | Delete a attachment |
| Get | `get` | Get a attachment |
| Get Many | `getAll` | Get many attachments |
| Get Summary | `getSummary` | Returns an overview of attachment's metadata |
| Update | `update` | Update a attachment |

### User Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a user |
| Get Many | `getAll` | Get many users |

### Flow Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many flows |
| Invoke | `invoke` | Invoke a flow |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | lead | ✗ | Represents an individual account, which is an organization or person involved with your business (such as customers, competitors, and partners) |  |

**Resource options:**

* **Account** (`account`) - Represents an individual account, which is an organization or person involved with your business (such as customers, competitors, and partners)
* **Attachment** (`attachment`) - Represents a file that a has uploaded and attached to a parent object
* **Case** (`case`) - Represents a case, which is a customer issue or problem
* **Contact** (`contact`) - Represents a contact, which is an individual associated with an account
* **Custom Object** (`customObject`) - Represents a custom object
* **Document** (`document`) - Represents a document
* **Flow** (`flow`) - Represents an autolaunched flow
* **Lead** (`lead`) - Represents a prospect or potential
* **Opportunity** (`opportunity`) - Represents an opportunity, which is a sale or pending deal
* **Search** (`search`) - Search records
* **Task** (`task`) - Represents a business activity such as making a phone call or other to-do items. In the user interface, and records are collectively referred to as activities.
* **User** (`user`) - Represents a person, which is one user in system

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Add lead to a campaign |  |

**Operation options:**

* **Add Lead To Campaign** (`addToCampaign`) - Add lead to a campaign
* **Add Note** (`addNote`) - Add note to a lead
* **Create** (`create`) - Create a lead
* **Create or Update** (`upsert`) - Create a new lead, or update the current one if it already exists (upsert)
* **Delete** (`delete`) - Delete a lead
* **Get** (`get`) - Get a lead
* **Get Many** (`getAll`) - Get many leads
* **Get Summary** (`getSummary`) - Returns an overview of Lead's metadata
* **Update** (`update`) - Update a lead

---

### Add Lead To Campaign parameters (`addToCampaign`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Lead ID | `leadId` | string |  | ✓ | ID of contact that needs to be fetched |  |
| Campaign Name or ID | `campaignId` | options |  | ✓ | ID of the campaign that needs to be fetched. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Options | `options` | collection | {} | ✗ | Controls the HasResponded flag on this object | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Status | `status` | string |  | Controls the HasResponded flag on this object |

</details>

| Contact ID | `contactId` | string |  | ✓ | ID of contact that needs to be fetched |  |
| Campaign Name or ID | `campaignId` | options |  | ✓ | ID of the campaign that needs to be fetched. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Options | `options` | collection | {} | ✗ | Controls the HasResponded flag on this object | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Status | `status` | string |  | Controls the HasResponded flag on this object |

</details>


### Add Note parameters (`addNote`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Lead ID | `leadId` | string |  | ✓ | ID of lead that needs to be fetched |  |
| Title | `title` | string |  | ✓ | Title of the note |  |
| Options | `options` | collection | {} | ✗ | Body of the note. Limited to 32 KB. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Body | `body` | string |  | Body of the note. Limited to 32 KB. |
| Is Private | `isPrivate` | boolean | False | Whether true, only the note owner or a user with the “Modify All Data” permission can view the note or query it via the API |
| Owner Name or ID | `owner` | options |  | ID of the user who owns the note. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Contact ID | `contactId` | string |  | ✓ | ID of contact that needs to be fetched |  |
| Title | `title` | string |  | ✓ | Title of the note |  |
| Options | `options` | collection | {} | ✗ | Body of the note. Limited to 32 KB. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Body | `body` | string |  | Body of the note. Limited to 32 KB. |
| Is Private | `isPrivate` | boolean | False | Whether only the note owner or a user with the “Modify All Data” permission can view the note or query it via the API |
| Owner Name or ID | `owner` | options |  | ID of the user who owns the note. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Opportunity ID | `opportunityId` | string |  | ✓ | ID of opportunity that needs to be fetched |  |
| Title | `title` | string |  | ✓ | Title of the note |  |
| Options | `options` | collection | {} | ✗ | Body of the note. Limited to 32 KB. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Body | `body` | string |  | Body of the note. Limited to 32 KB. |
| Is Private | `isPrivate` | boolean | False | Whether true, only the note owner or a user with the “Modify All Data” permission can view the note or query it via the API |
| Owner Name or ID | `owner` | options |  | ID of the user who owns the note. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Account ID | `accountId` | string |  | ✓ | ID of account that needs to be fetched |  |
| Title | `title` | string |  | ✓ | Title of the note |  |
| Options | `options` | collection | {} | ✗ | Body of the note. Limited to 32 KB. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Body | `body` | string |  | Body of the note. Limited to 32 KB. |
| Is Private | `isPrivate` | boolean | False | Whether true, only the note owner or a user with the “Modify All Data” permission can view the note or query it via the API |
| Owner Name or ID | `ownerId` | options |  | ID of the user who owns the note. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Company | `company` | string |  | ✓ | Company of the lead. If person account record types have been enabled, and if the value of Company is null, the lead converts to a person account. |  |
| Last Name | `lastname` | string |  | ✓ | Required. Last name of the lead. Limited to 80 characters. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Annual revenue for the company of the lead | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Annual Revenue | `annualRevenue` | number |  | Annual revenue for the company of the lead |
| City | `city` | string |  | City for the address of the lead |
| Country | `country` | string |  | Country of the lead |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Description | `description` | string |  | Description of the lead |
| Email | `email` | string |  | Email address for the lead |
| Fax | `fax` | number |  | Fax number of the lead |
| First Name | `firstname` | string |  | First name of the lead. Limited to 40 characters. |
| Has Opted Out of Email | `hasOptedOutOfEmail` | boolean | False | Whether the lead doesn’t want to receive email from Salesforce (true) or does (false). Label is Email Opt Out. |
| Has Opted Out of Fax | `hasOptedOutOfFax` | boolean | False | Whether the lead doesn’t want to receive fax from Salesforce (true) or does (false). Label is Email Opt Out. |
| Industry | `industry` | string |  | Website for the lead |
| Is Unread By Owner | `IsUnreadByOwner` | boolean | False | Whether true, lead has been assigned, but not yet viewed. See Unread Leads for more information. Label is Unread By Owner. |
| Jigsaw | `jigsaw` | string |  | References the ID of a contact in Data.com. If a lead has a value in this field, it means that a contact was imported as a lead from Data.com. |
| Lead Source Name or ID | `leadSource` | options |  | Source from which the lead was obtained. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Mobile Phone | `mobilePhone` | string |  | Contact’s mobile phone number |
| Number Of Employees | `numberOfEmployees` | number |  | Number of employees at the lead’s company. Label is Employees. |
| Owner Name or ID | `owner` | options |  | The owner of the lead. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Phone | `phone` | string |  | Phone number for the lead |
| Postal Code | `postalCode` | string |  | Postal code for the address of the lead. Label is Zip/Postal Code. |
| Record Type Name or ID | `recordTypeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Rating | `rating` | string |  | Rating of the lead |
| Salutation | `salutation` | string |  | Salutation for the lead |
| State | `state` | string |  | State for the address of the lead |
| Status Name or ID | `status` | options |  | Status code for this converted lead. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Street | `street` | string |  | Street number and name for the address of the lead |
| Title | `title` | string |  | Title for the lead, for example CFO or CEO |
| Website | `website` | string |  | Website for the lead |

</details>

| Last Name | `lastname` | string |  | ✓ | Required. Last name of the contact. Limited to 80 characters. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the account that is the parent of this contact. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Name or ID | `acconuntId` | options |  | ID of the account that is the parent of this contact. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Assistant Name | `assistantName` | string |  | The name of the assistant |
| Assistant Phone | `Assistant Phone` | string |  | The telephone number of the assistant |
| Birth Date | `birthdate` | dateTime |  | The birth date of the contact |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Department | `department` | string |  | The department of the contact |
| Description | `description` | string |  | A description of the contact. Label is Contact Description. Limit: 32 KB. |
| Email | `email` | string |  | Email address for the contact |
| Email Bounced Date | `otherPostalCode` | dateTime |  | If bounce management is activated and an email sent to the contact bounces, the date and time the bounce occurred |
| Email Bounced Reason | `emailBouncedReason` | string |  | If bounce management is activated and an email sent to the contact bounces, the reason the bounce occurred |
| Fax | `fax` | string |  | Fax number for the contact. Label is Business Fax. |
| First Name | `firstName` | string |  | First name of the contact. Maximum size is 40 characters. |
| Home Phone | `homePhone` | string |  | Home telephone number for the contact |
| Jigsaw | `jigsaw` | string |  | References the ID of a contact in Data.com. If a contact has a value in this field, it means that a contact was imported as a contact from Data.com. |
| Lead Source Name or ID | `leadSource` | options |  | Source from which the lead was obtained. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Mailing City | `mailingCity` | string |  |  |
| Mailing Country | `mailingCountry` | string |  |  |
| Mobile Phone | `mobilePhone` | string |  | Contact’s mobile phone number |
| Mailing Postal Code | `mailingPostalCode` | string |  |  |
| Mailing State | `mailingState` | string |  |  |
| Mailing Street | `mailingStreet` | string |  | Street address for mailing address |
| Other City | `otherCity` | string |  |  |
| Other Country | `otherCountry` | string |  |  |
| Other Phone | `otherPhone` | string |  | Telephone for alternate address |
| Other Postal Code | `otherPostalCode` | string |  |  |
| Other State | `otherState` | string |  |  |
| Other Street | `otherStreet` | string |  | Street for alternate address |
| Owner Name or ID | `owner` | options |  | The owner of the contact. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Phone | `phone` | string |  | Phone number for the contact |
| Record Type Name or ID | `recordTypeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Salutation | `salutation` | string |  | Honorific abbreviation, word, or phrase to be used in front of name in greetings, such as Dr. or Mrs. |
| Title | `title` | string |  | Title of the contact such as CEO or Vice President |

</details>

| Custom Object Name or ID | `customObject` | options |  | ✓ | Name of the custom object. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Fields | `customFieldsUi` | fixedCollection | {} | ✗ | Filter by custom fields | e.g. Add Field |  |

<details>
<summary><strong>Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Field | `customFieldsValues` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Record Type Name or ID | `recordTypeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Name | `name` | string |  | ✓ | Required. Last name of the opportunity. Limited to 80 characters. |  |
| Close Date | `closeDate` | dateTime |  | ✓ | Required. Date when the opportunity is expected to close. |  |
| Stage Name or ID | `stageName` | options |  | ✓ | Required. Date when the opportunity is expected to close. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the account associated with this opportunity. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Name or ID | `accountId` | options |  | ID of the account associated with this opportunity. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Amount | `amount` | number |  | Estimated total sale amount |
| Campaign Name or ID | `campaignId` | options |  | ID of the campaign that needs to be fetched. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Description | `description` | string |  | A description of the opportunity. Label is Contact Description. Limit: 32 KB. |
| Forecast Category Name | `forecastCategoryName` | string |  | It is implied, but not directly controlled, by the StageName field |
| Lead Source Name or ID | `leadSource` | options |  | Source from which the lead was obtained. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Next Step | `nextStep` | string |  | Description of next task in closing opportunity. Limit: 255 characters. |
| Owner Name or ID | `owner` | options |  | The owner of the opportunity. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Phone | `phone` | string |  | Phone number for the opportunity |
| Pricebook2 ID | `pricebook2Id` | string |  | ID of a related Pricebook2 object |
| Probability | `probability` | number |  | Percentage of estimated confidence in closing the opportunity |
| Type | `type` | options |  | Type of opportunity. For example, Existing Business or New Business. Label is Opportunity Type. |

</details>

| Name | `name` | string |  | ✓ | Name of the account. Maximum size is 255 characters. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Account number assigned to this account (not the unique ID). Maximum size is 40 characters. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Number | `accountNumber` | string |  | Account number assigned to this account (not the unique ID). Maximum size is 40 characters. |
| Annual Revenue | `annualRevenue` | number |  | Estimated annual revenue of the account |
| Account Source Name or ID | `accountSource` | options |  | The source of the account record. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Billing City | `billingCity` | string |  | Details for the billing address of this account. Maximum size is 40 characters. |
| Billing Country | `billingCountry` | string |  | Details for the billing address of this account. Maximum size is 80 characters. |
| Billing Postal Code | `billingPostalCode` | string |  | Details for the billing address of this account. Maximum size is 20 characters. |
| Billing State | `billingState` | string |  | Details for the billing address of this account. Maximum size is 80 characters. |
| Billing Street | `billingStreet` | string |  | Street address for the billing address of this account |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Description | `description` | string |  | Text description of the account. Limited to 32,000 KB. |
| Fax | `fax` | string |  | Fax number for the account |
| Jigsaw | `jigsaw` | string |  | References the ID of a company in Data.com |
| Industry | `industry` | string |  | The website of this account. Maximum of 255 characters. |
| Number Of Employees | `numberOfEmployees` | number |  |  |
| Owner Name or ID | `owner` | options |  | The owner of the account. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Parent ID | `parentId` | string |  | ID of the parent object, if any |
| Phone | `phone` | string |  | Phone number for the account |
| Record Type Name or ID | `recordTypeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| SicDesc | `sicDesc` | string |  | A brief description of an organization’s line of business, based on its SIC code |
| Type Name or ID | `type` | options |  | Type of account. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Shipping City | `shippingCity` | string |  | Details of the shipping address for this account. City maximum size is 40 characters. |
| Shipping Country | `shippingCountry` | string |  | Details of the shipping address for this account. Country maximum size is 80 characters. |
| Shipping Postal Code | `shippingPostalCode` | string |  | Details of the shipping address for this account. Postal code maximum size is 20 characters. |
| Shipping State | `shippingState` | string |  | Details of the shipping address for this account. State maximum size is 80 characters. |
| Shipping Street | `shippingStreet` | string |  | The street address of the shipping address for this account. Maximum of 255 characters. |
| Website | `website` | string |  | The website of this account. Maximum of 255 characters. |

</details>

| Type Name or ID | `type` | options |  | ✓ | The type of case. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the account associated with this case | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account ID | `accountId` | string |  | ID of the account associated with this case |
| Contact ID | `contactId` | string |  | ID of the associated Contact |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Description | `description` | string |  | A text description of the case. Limit: 32 KB. |
| Is Escalated | `isEscalated` | boolean | False | Whether indicates whether the case has been escalated (true) or not |
| Origin Name or ID | `origin` | options |  | The source of the case, such as Email, Phone, or Web. Label is Case Origin. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Owner Name or ID | `owner` | options |  | The owner of the case. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Parent ID | `ParentId` | string |  | The ID of the parent case in the hierarchy. The label is Parent Case. |
| Priority Name or ID | `priority` | options |  | The importance or urgency of the case, such as High, Medium, or Low. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Reason Name or ID | `reason` | options |  | The reason why the case was created, such as Instructions not clear, or User didn’t attend training. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Record Type Name or ID | `recordTypeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Status Name or ID | `status` | options |  | The status of the case, such as “New,” “Closed,” or “Escalated.” This field directly controls the IsClosed flag. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Subject | `subject` | string |  | The subject of the case. Limit: 255 characters. |
| Supplied Company | `suppliedCompany` | string |  | The company name that was entered when the case was created. This field can't be updated after the case has been created.. |
| Supplied Email | `suppliedEmail` | string |  | The email address that was entered when the case was created. This field can't be updated after the case has been created. |
| Supplied Name | `suppliedName` | string |  | The name that was entered when the case was created. This field can't be updated after the case has been created. |
| Supplied Phone | `suppliedPhone` | string |  | The phone number that was entered when the case was created. This field can't be updated after the case has been created. |

</details>

| Status Name or ID | `status` | options |  | ✓ | The current status of the task, such as In Progress or Completed. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Represents the due date of the task. This field has a timestamp that is always set to midnight in the Coordinated Universal Time (UTC) time zone. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Activity Date | `activityDate` | dateTime |  | Represents the due date of the task. This field has a timestamp that is always set to midnight in the Coordinated Universal Time (UTC) time zone. |
| Call Disposition | `callDisposition` | string |  | Represents the result of a given call, for example, “we'll call back,” or “call unsuccessful.” Limit is 255 characters. Not subject to field-level security, available for any user in an organization with Salesforce CRM Call Center. |
| Call Duration In Seconds | `callDurationInSeconds` | number |  | Duration of the call in seconds. Not subject to field-level security, available for any user in an organization with Salesforce CRM Call Center. |
| Call Object | `callObject` | string |  | Name of a call center. Limit is 255 characters. Not subject to field-level security, available for any user in an organization with Salesforce CRM Call Center. |
| Call Type Name or ID | `callType` | options |  | The type of call being answered: Inbound, Internal, or Outbound. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Description | `description` | string |  | Contains a text description of the task |
| Is ReminderSet | `isReminderSet` | boolean | False | Whether a popup reminder has been set for the task (true) or not (false) |
| Owner Name or ID | `owner` | options |  | ID of the User who owns the record. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Priority Name or ID | `priority` | options |  | Indicates the importance or urgency of a task, such as high or low. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Recurrence Type Name or ID | `recurrenceType` | options |  | Recurrence Type of the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Recurrence Instance Name or ID | `recurrenceInstance` | options |  | The frequency of the recurring task. For example, “2nd” or “3rd.”. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Recurrence Interval | `recurrenceInterval` | number |  | The interval between recurring tasks |
| Recurrence Day Of Month | `recurrenceDayOfMonth` | number |  | The day of the month in which the task repeats |
| Recurrence Day Of Week Mask | `recurrenceDayOfWeekMask` | number |  | The day or days of the week on which the task repeats. This field contains a bitmask. The values are as follows: Sunday = 1 Monday = 2 Tuesday = 4 Wednesday = 8 Thursday = 16 Friday = 32 Saturday = 64 Multiple days are represented as the sum of their numerical values. For example, Tuesday and Thursday = 4 + 16 = 20. |
| Recurrence End Date Only | `recurrenceEndDateOnly` | dateTime |  | The last date on which the task repeats. This field has a timestamp that is always set to midnight in the Coordinated Universal Time (UTC) time zone. |
| Recurrence Month Of Year | `recurrenceMonthOfYear` | options |  | The month of the year in which the task repeats |
| Recurrence Regenerated Type | `recurrenceRegeneratedType` | options |  | Represents what triggers a repeating task to repeat. Add this field to a page layout together with the RecurrenceInterval field, which determines the number of days between the triggering date (due date or close date) and the due date of the next repeating task in the series. Label is Repeat This Task. |
| Recurrence Start Date Only | `recurrenceEndDateOnly` | dateTime |  | The date when the recurring task begins. Must be a date and time before RecurrenceEndDateOnly. |
| Recurrence TimeZone SidKey | `recurrenceTimeZoneSidKey` | string |  | The time zone associated with the recurring task. For example, “UTC-8:00” for Pacific Standard Time. |
| Reminder Date Time | `reminderDateTime` | dateTime |  | Represents the time when the reminder is scheduled to fire, if IsReminderSet is set to true. If IsReminderSet is set to false, then the user may have deselected the reminder checkbox in the Salesforce user interface, or the reminder has already fired at the time indicated by the value. |
| Subject Name or ID | `subject` | options |  | The subject line of the task, such as “Call” or “Send Quote.” Limit: 255 characters. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Type Name or ID | `type` | options |  | Represents Type of the task, such as Call or Meeting. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| What ID | `whatId` | string |  | The WhatId represents nonhuman objects such as accounts, opportunities, campaigns, cases, or custom objects. WhatIds are polymorphic. Polymorphic means a WhatId is equivalent to the ID of a related object. |
| Who ID | `whoId` | string |  | The WhoId represents a human such as a lead or a contact. WhoIds are polymorphic. Polymorphic means a WhoId is equivalent to a contact’s ID or a lead’s ID. |

</details>

| Parent ID | `parentId` | string |  | ✓ |  |  |
| Name | `name` | string |  | ✓ | Required. Name of the attached file. Maximum size is 255 characters. Label is File Name. |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be uploaded |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Text description of the Document. Limit: 255 characters. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | Text description of the Document. Limit: 255 characters. |
| Is Private | `isPrivate` | boolean | False | Whether this record is viewable only by the owner and administrators (true) or viewable by all otherwise-allowed users (false) |
| Owner Name or ID | `owner` | options |  | ID of the User who owns the attachment. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Create or Update parameters (`upsert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Match Against | `externalId` | options |  | ✓ | The field to check to see if the lead already exists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Value to Match | `externalIdValue` | string |  | ✓ | If this value exists in the 'match against' field, update the lead. Otherwise create a new one. |  |
| Company | `company` | string |  | ✓ | Company of the lead. If person account record types have been enabled, and if the value of Company is null, the lead converts to a person account. |  |
| Last Name | `lastname` | string |  | ✓ | Required. Last name of the lead. Limited to 80 characters. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Annual revenue for the company of the lead | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Annual Revenue | `annualRevenue` | number |  | Annual revenue for the company of the lead |
| City | `city` | string |  | City for the address of the lead |
| Country | `country` | string |  | Country of the lead |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Description | `description` | string |  | Description of the lead |
| Email | `email` | string |  | Email address for the lead |
| Fax | `fax` | number |  | Fax number of the lead |
| First Name | `firstname` | string |  | First name of the lead. Limited to 40 characters. |
| Has Opted Out of Email | `hasOptedOutOfEmail` | boolean | False | Whether the lead doesn’t want to receive email from Salesforce (true) or does (false). Label is Email Opt Out. |
| Has Opted Out of Fax | `hasOptedOutOfFax` | boolean | False | Whether the lead doesn’t want to receive fax from Salesforce (true) or does (false). Label is Email Opt Out. |
| Industry | `industry` | string |  | Website for the lead |
| Is Unread By Owner | `IsUnreadByOwner` | boolean | False | Whether true, lead has been assigned, but not yet viewed. See Unread Leads for more information. Label is Unread By Owner. |
| Jigsaw | `jigsaw` | string |  | References the ID of a contact in Data.com. If a lead has a value in this field, it means that a contact was imported as a lead from Data.com. |
| Lead Source Name or ID | `leadSource` | options |  | Source from which the lead was obtained. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Mobile Phone | `mobilePhone` | string |  | Contact’s mobile phone number |
| Number Of Employees | `numberOfEmployees` | number |  | Number of employees at the lead’s company. Label is Employees. |
| Owner Name or ID | `owner` | options |  | The owner of the lead. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Phone | `phone` | string |  | Phone number for the lead |
| Postal Code | `postalCode` | string |  | Postal code for the address of the lead. Label is Zip/Postal Code. |
| Record Type Name or ID | `recordTypeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Rating | `rating` | string |  | Rating of the lead |
| Salutation | `salutation` | string |  | Salutation for the lead |
| State | `state` | string |  | State for the address of the lead |
| Status Name or ID | `status` | options |  | Status code for this converted lead. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Street | `street` | string |  | Street number and name for the address of the lead |
| Title | `title` | string |  | Title for the lead, for example CFO or CEO |
| Website | `website` | string |  | Website for the lead |

</details>

| Match Against | `externalId` | options |  | ✓ | The field to check to see if the contact already exists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Value to Match | `externalIdValue` | string |  | ✓ | If this value exists in the 'match against' field, update the contact. Otherwise create a new one. |  |
| Last Name | `lastname` | string |  | ✓ | Required. Last name of the contact. Limited to 80 characters. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the account that is the parent of this contact. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Name or ID | `acconuntId` | options |  | ID of the account that is the parent of this contact. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Assistant Name | `assistantName` | string |  | The name of the assistant |
| Assistant Phone | `Assistant Phone` | string |  | The telephone number of the assistant |
| Birth Date | `birthdate` | dateTime |  | The birth date of the contact |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Department | `department` | string |  | The department of the contact |
| Description | `description` | string |  | A description of the contact. Label is Contact Description. Limit: 32 KB. |
| Email | `email` | string |  | Email address for the contact |
| Email Bounced Date | `otherPostalCode` | dateTime |  | If bounce management is activated and an email sent to the contact bounces, the date and time the bounce occurred |
| Email Bounced Reason | `emailBouncedReason` | string |  | If bounce management is activated and an email sent to the contact bounces, the reason the bounce occurred |
| Fax | `fax` | string |  | Fax number for the contact. Label is Business Fax. |
| First Name | `firstName` | string |  | First name of the contact. Maximum size is 40 characters. |
| Home Phone | `homePhone` | string |  | Home telephone number for the contact |
| Jigsaw | `jigsaw` | string |  | References the ID of a contact in Data.com. If a contact has a value in this field, it means that a contact was imported as a contact from Data.com. |
| Lead Source Name or ID | `leadSource` | options |  | Source from which the lead was obtained. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Mailing City | `mailingCity` | string |  |  |
| Mailing Country | `mailingCountry` | string |  |  |
| Mobile Phone | `mobilePhone` | string |  | Contact’s mobile phone number |
| Mailing Postal Code | `mailingPostalCode` | string |  |  |
| Mailing State | `mailingState` | string |  |  |
| Mailing Street | `mailingStreet` | string |  | Street address for mailing address |
| Other City | `otherCity` | string |  |  |
| Other Country | `otherCountry` | string |  |  |
| Other Phone | `otherPhone` | string |  | Telephone for alternate address |
| Other Postal Code | `otherPostalCode` | string |  |  |
| Other State | `otherState` | string |  |  |
| Other Street | `otherStreet` | string |  | Street for alternate address |
| Owner Name or ID | `owner` | options |  | The owner of the contact. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Phone | `phone` | string |  | Phone number for the contact |
| Record Type Name or ID | `recordTypeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Salutation | `salutation` | string |  | Honorific abbreviation, word, or phrase to be used in front of name in greetings, such as Dr. or Mrs. |
| Title | `title` | string |  | Title of the contact such as CEO or Vice President |

</details>

| Custom Object Name or ID | `customObject` | options |  | ✓ | Name of the custom object. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Match Against | `externalId` | options |  | ✓ | The field to check to see if the object already exists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Value to Match | `externalIdValue` | string |  | ✓ | If this value exists in the 'match against' field, update the object. Otherwise create a new one. |  |
| Fields | `customFieldsUi` | fixedCollection | {} | ✗ | Filter by custom fields | e.g. Add Field |  |

<details>
<summary><strong>Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Field | `customFieldsValues` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Record Type Name or ID | `recordTypeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Match Against | `externalId` | options |  | ✓ | The field to check to see if the opportunity already exists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Value to Match | `externalIdValue` | string |  | ✓ | If this value exists in the 'match against' field, update the opportunity. Otherwise create a new one. |  |
| Name | `name` | string |  | ✓ | Required. Last name of the opportunity. Limited to 80 characters. |  |
| Close Date | `closeDate` | dateTime |  | ✓ | Required. Date when the opportunity is expected to close. |  |
| Stage Name or ID | `stageName` | options |  | ✓ | Required. Date when the opportunity is expected to close. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the account associated with this opportunity. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Name or ID | `accountId` | options |  | ID of the account associated with this opportunity. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Amount | `amount` | number |  | Estimated total sale amount |
| Campaign Name or ID | `campaignId` | options |  | ID of the campaign that needs to be fetched. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Description | `description` | string |  | A description of the opportunity. Label is Contact Description. Limit: 32 KB. |
| Forecast Category Name | `forecastCategoryName` | string |  | It is implied, but not directly controlled, by the StageName field |
| Lead Source Name or ID | `leadSource` | options |  | Source from which the lead was obtained. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Next Step | `nextStep` | string |  | Description of next task in closing opportunity. Limit: 255 characters. |
| Owner Name or ID | `owner` | options |  | The owner of the opportunity. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Phone | `phone` | string |  | Phone number for the opportunity |
| Pricebook2 ID | `pricebook2Id` | string |  | ID of a related Pricebook2 object |
| Probability | `probability` | number |  | Percentage of estimated confidence in closing the opportunity |
| Type | `type` | options |  | Type of opportunity. For example, Existing Business or New Business. Label is Opportunity Type. |

</details>

| Match Against | `externalId` | options |  | ✓ | The field to check to see if the account already exists. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Value to Match | `externalIdValue` | string |  | ✓ | If this value exists in the 'match against' field, update the account. Otherwise create a new one. |  |
| Name | `name` | string |  | ✓ | Name of the account. Maximum size is 255 characters. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Account number assigned to this account (not the unique ID). Maximum size is 40 characters. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Number | `accountNumber` | string |  | Account number assigned to this account (not the unique ID). Maximum size is 40 characters. |
| Annual Revenue | `annualRevenue` | number |  | Estimated annual revenue of the account |
| Account Source Name or ID | `accountSource` | options |  | The source of the account record. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Billing City | `billingCity` | string |  | Details for the billing address of this account. Maximum size is 40 characters. |
| Billing Country | `billingCountry` | string |  | Details for the billing address of this account. Maximum size is 80 characters. |
| Billing Postal Code | `billingPostalCode` | string |  | Details for the billing address of this account. Maximum size is 20 characters. |
| Billing State | `billingState` | string |  | Details for the billing address of this account. Maximum size is 80 characters. |
| Billing Street | `billingStreet` | string |  | Street address for the billing address of this account |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Description | `description` | string |  | Text description of the account. Limited to 32,000 KB. |
| Fax | `fax` | string |  | Fax number for the account |
| Jigsaw | `jigsaw` | string |  | References the ID of a company in Data.com |
| Industry | `industry` | string |  | The website of this account. Maximum of 255 characters. |
| Number Of Employees | `numberOfEmployees` | number |  |  |
| Owner Name or ID | `owner` | options |  | The owner of the account. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Parent ID | `parentId` | string |  | ID of the parent object, if any |
| Phone | `phone` | string |  | Phone number for the account |
| Record Type Name or ID | `recordTypeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| SicDesc | `sicDesc` | string |  | A brief description of an organization’s line of business, based on its SIC code |
| Type Name or ID | `type` | options |  | Type of account. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Shipping City | `shippingCity` | string |  | Details of the shipping address for this account. City maximum size is 40 characters. |
| Shipping Country | `shippingCountry` | string |  | Details of the shipping address for this account. Country maximum size is 80 characters. |
| Shipping Postal Code | `shippingPostalCode` | string |  | Details of the shipping address for this account. Postal code maximum size is 20 characters. |
| Shipping State | `shippingState` | string |  | Details of the shipping address for this account. State maximum size is 80 characters. |
| Shipping Street | `shippingStreet` | string |  | The street address of the shipping address for this account. Maximum of 255 characters. |
| Website | `website` | string |  | The website of this account. Maximum of 255 characters. |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Lead ID | `leadId` | string |  | ✓ | ID of Lead that needs to be fetched |  |
| Contact ID | `contactId` | string |  | ✓ | ID of contact that needs to be fetched |  |
| Custom Object Name or ID | `customObject` | options |  | ✓ | Name of the custom object. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Record ID | `recordId` | string |  | ✓ | Record ID to be deleted |  |
| Opportunity ID | `opportunityId` | string |  | ✓ | ID of opportunity that needs to be fetched |  |
| Account ID | `accountId` | string |  | ✓ | ID of account that needs to be fetched |  |
| Case ID | `caseId` | string |  | ✓ | ID of case that needs to be fetched |  |
| Task ID | `taskId` | string |  | ✓ | ID of task that needs to be fetched |  |
| Attachment ID | `attachmentId` | string |  | ✓ | ID of attachment that needs to be fetched |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Lead ID | `leadId` | string |  | ✓ | ID of Lead that needs to be fetched |  |
| Contact ID | `contactId` | string |  | ✓ | ID of contact that needs to be fetched |  |
| Custom Object Name or ID | `customObject` | options |  | ✓ | Name of the custom object. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Record ID | `recordId` | string |  | ✓ | Record ID to be retrieved |  |
| Opportunity ID | `opportunityId` | string |  | ✓ | ID of opportunity that needs to be fetched |  |
| Account ID | `accountId` | string |  | ✓ | ID of account that needs to be fetched |  |
| Case ID | `caseId` | string |  | ✓ | ID of case that needs to be fetched |  |
| Task ID | `taskId` | string |  | ✓ | ID of task that needs to be fetched |  |
| Attachment ID | `attachmentId` | string |  | ✓ | ID of attachment that needs to be fetched |  |
| User ID | `userId` | string |  | ✓ | ID of user that needs to be fetched |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | The condition to set | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Conditions | `conditionsUi` | fixedCollection | {} | The condition to set |
| Fields | `fields` | string |  | Fields to include separated by , |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | The condition to set | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Conditions | `conditionsUi` | fixedCollection | {} | The condition to set |
| Fields | `fields` | string |  | Fields to include separated by , |

</details>

| Custom Object Name or ID | `customObject` | options |  | ✓ | Name of the custom object. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | The condition to set | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Conditions | `conditionsUi` | fixedCollection | {} | The condition to set |
| Field Names or IDs | `fields` | multiOptions | [] | Fields to include separated by commas. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | The condition to set | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Conditions | `conditionsUi` | fixedCollection | {} | The condition to set |
| Fields | `fields` | string |  | Fields to include separated by , |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | Fields to include separated by , | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | Fields to include separated by , |
| Conditions | `conditionsUi` | fixedCollection | {} | The condition to set |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | The condition to set | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Conditions | `conditionsUi` | fixedCollection | {} | The condition to set |
| Fields | `fields` | string |  | Fields to include separated by , |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | The condition to set | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Conditions | `conditionsUi` | fixedCollection | {} | The condition to set |
| Fields | `fields` | string |  | Fields to include separated by , |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | The condition to set | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Conditions | `conditionsUi` | fixedCollection | {} | The condition to set |
| Fields | `fields` | string |  | Fields to include separated by , |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | The condition to set | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Conditions | `conditionsUi` | fixedCollection | {} | The condition to set |
| Fields | `fields` | string |  | Fields to include separated by , |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:500 |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Lead ID | `leadId` | string |  | ✓ | ID of Lead that needs to be fetched |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Annual revenue for the company of the lead | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Annual Revenue | `annualRevenue` | number |  | Annual revenue for the company of the lead |
| City | `city` | string |  | City for the address of the lead |
| Company | `company` | string |  | Company of the lead. If person account record types have been enabled, and if the value of Company is null, the lead converts to a person account. |
| Country | `country` | string |  | Country of the lead |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Description | `description` | string |  | Description of the lead |
| Email | `email` | string |  | Email address for the lead |
| Fax | `fax` | number |  | Fax Number of the lead |
| First Name | `firstname` | string |  | First name of the lead. Limited to 40 characters. |
| Has Opted Out of Email | `hasOptedOutOfEmail` | boolean | False | Whether the lead doesn’t want to receive email from Salesforce (true) or does (false). Label is Email Opt Out. |
| Has Opted Out of Fax | `HasOptedOutOfFax` | boolean | False | Whether the lead doesn’t want to receive fax from Salesforce (true) or does (false). Label is Fax Opt Out. |
| Industry | `industry` | string |  | Website for the lead |
| Is Unread By Owner | `IsUnreadByOwner` | boolean | False | Whether true, lead has been assigned, but not yet viewed. See Unread Leads for more information. Label is Unread By Owner. |
| Jigsaw | `jigsaw` | string |  | References the ID of a contact in Data.com. If a lead has a value in this field, it means that a contact was imported as a lead from Data.com. |
| Last Name | `lastname` | string |  | Required. Last name of the lead. Limited to 80 characters. |
| Lead Source Name or ID | `leadSource` | options |  | Source from which the lead was obtained. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Mobile Phone | `mobilePhone` | string |  | Contact’s mobile phone number |
| Number Of Employees | `numberOfEmployees` | number |  | Number of employees at the lead’s company. Label is Employees. |
| Owner Name or ID | `owner` | options |  | The owner of the lead. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Postal Code | `postalCode` | string |  | Postal code for the address of the lead. Label is Zip/Postal Code. |
| Phone | `phone` | string |  | Phone number for the lead |
| Record Type Name or ID | `recordTypeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Rating | `rating` | string |  | Rating of the lead |
| Salutation | `salutation` | string |  | Salutation for the lead |
| State | `state` | string |  | State for the address of the lead |
| Status Name or ID | `status` | options |  | Status code for this converted lead. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Street | `street` | string |  | Street number and name for the address of the lead |
| Title | `title` | string |  | Title for the lead, for example CFO or CEO |
| Website | `website` | string |  | Website for the lead |

</details>

| Contact ID | `contactId` | string |  | ✓ | ID of contact that needs to be fetched |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the account that is the parent of this contact. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Name or ID | `acconuntId` | options |  | ID of the account that is the parent of this contact. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Assistant Name | `assistantName` | string |  | The name of the assistant |
| Assistant Phone | `Assistant Phone` | string |  | The telephone number of the assistant |
| Birth Date | `birthdate` | dateTime |  | The birth date of the contact |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Department | `department` | string |  | The department of the contact |
| Description | `description` | string |  | A description of the contact. Label is Contact Description. Limit: 32 KB. |
| Email | `email` | string |  | Email address for the contact |
| Email Bounced Date | `emailBouncedDate` | dateTime |  | If bounce management is activated and an email sent to the contact bounces, the date and time the bounce occurred |
| Email Bounced Reason | `emailBouncedReason` | string |  | If bounce management is activated and an email sent to the contact bounces, the reason the bounce occurred |
| Fax | `fax` | string |  | Fax number for the contact. Label is Business Fax. |
| First Name | `firstName` | string |  | First name of the contact. Maximum size is 40 characters. |
| Home Phone | `homePhone` | string |  | Home telephone number for the contact |
| Jigsaw | `jigsaw` | string |  | References the ID of a contact in Data.com. If a contact has a value in this field, it means that a contact was imported as a contact from Data.com. |
| Last Name | `lastName` | string |  | Last name of the contact. Limited to 80 characters. |
| Lead Source Name or ID | `leadSource` | options |  | Source from which the lead was obtained. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Mailing City | `mailingCity` | string |  |  |
| Mailing Country | `mailingCountry` | string |  |  |
| Mailing State | `mailingState` | string |  |  |
| Mailing Street | `mailingStreet` | string |  | Street address for mailing address |
| Mailing Postal Code | `mailingPostalCode` | string |  |  |
| Mobile Phone | `mobilePhone` | string |  | Contact’s mobile phone number |
| Other City | `otherCity` | string |  |  |
| Other Country | `otherCountry` | string |  |  |
| Other Phone | `otherPhone` | string |  | Telephone for alternate address |
| Other Postal Code | `otherPostalCode` | string |  |  |
| Other State | `otherState` | string |  |  |
| Other Street | `otherStreet` | string |  | Street for alternate address |
| Owner Name or ID | `owner` | options |  | The owner of the contact. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Phone | `phone` | string |  | Phone number for the contact |
| Record Type Name or ID | `recordTypeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Salutation | `salutation` | string |  | Honorific abbreviation, word, or phrase to be used in front of name in greetings, such as Dr. or Mrs. |
| Title | `title` | string |  | Title of the contact such as CEO or Vice President |

</details>

| Custom Object Name or ID | `customObject` | options |  | ✓ | Name of the custom object. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Record ID | `recordId` | string |  | ✓ | Record ID to be updated |  |
| Fields | `customFieldsUi` | fixedCollection | {} | ✗ | Filter by custom fields | e.g. Add Field |  |

<details>
<summary><strong>Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Field | `customFieldsValues` |  |  |  |

</details>

| Update Fields | `updateFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Record Type Name or ID | `recordTypeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Opportunity ID | `opportunityId` | string |  | ✓ | ID of opportunity that needs to be fetched |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the account associated with this opportunity. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Name or ID | `accountId` | options |  | ID of the account associated with this opportunity. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Amount | `amount` | number |  | Estimated total sale amount |
| Campaign Name or ID | `campaignId` | options |  | ID of the campaign that needs to be fetched. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Close Date | `closeDate` | dateTime |  | Required. Date when the opportunity is expected to close. |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Description | `description` | string |  | A description of the opportunity. Label is Contact Description. Limit: 32 KB. |
| Forecast Category Name | `forecastCategoryName` | string |  | It is implied, but not directly controlled, by the StageName field |
| Lead Source Name or ID | `leadSource` | options |  | Source from which the lead was obtained. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Name | `name` | string |  | Required. Last name of the opportunity. Limited to 80 characters. |
| Next Step | `nextStep` | string |  | Description of next task in closing opportunity. Limit: 255 characters. |
| Owner Name or ID | `owner` | options |  | The owner of the opportunity. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Phone | `phone` | string |  | Phone number for the opportunity |
| Pricebook2 ID | `pricebook2Id` | string |  | ID of a related Pricebook2 object |
| Probability | `probability` | number |  | Percentage of estimated confidence in closing the opportunity |
| Stage Name or ID | `stageName` | options |  | Required. Date when the opportunity is expected to close. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Type | `type` | options |  | Type of opportunity. For example, Existing Business or New Business. Label is Opportunity Type. |

</details>

| Account ID | `accountId` | string |  | ✓ | ID of account that needs to be fetched |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Account number assigned to this account (not the unique ID). Maximum size is 40 characters. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Number | `accountNumber` | string |  | Account number assigned to this account (not the unique ID). Maximum size is 40 characters. |
| Account Source Name or ID | `accountSource` | options |  | The source of the account record. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Annual Revenue | `annualRevenue` | number |  | Estimated annual revenue of the account |
| Billing City | `billingCity` | string |  | Details for the billing address of this account. Maximum size is 40 characters. |
| Billing Country | `billingCountry` | string |  | Details for the billing address of this account. Maximum size is 80 characters. |
| Billing Postal Code | `billingPostalCode` | string |  | Details for the billing address of this account. Maximum size is 20 characters. |
| Billing State | `billingState` | string |  | Details for the billing address of this account. Maximum size is 80 characters. |
| Billing Street | `billingStreet` | string |  | Street address for the billing address of this account |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Description | `description` | string |  | Text description of the account. Limited to 32,000 KB. |
| Fax | `fax` | string |  | Fax number for the account |
| Industry | `industry` | string |  | The website of this account. Maximum of 255 characters. |
| Jigsaw | `jigsaw` | string |  | References the ID of a company in Data.com |
| Name | `name` | string |  | Name of the account. Maximum size is 255 characters. |
| Number Of Employees | `numberOfEmployees` | number |  |  |
| Owner Name or ID | `ownerId` | options |  | The owner of the account. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Parent ID | `parentId` | string |  | ID of the parent object, if any |
| Phone | `phone` | string |  | Phone number for the account |
| Record Type Name or ID | `recordTypeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| SicDesc | `sicDesc` | string |  | A brief description of an organization’s line of business, based on its SIC code |
| Shipping City | `shippingCity` | string |  | Details of the shipping address for this account. City maximum size is 40 characters. |
| Shipping Country | `shippingCountry` | string |  | Details of the shipping address for this account. Country maximum size is 80 characters. |
| Shipping Postal Code | `shippingPostalCode` | string |  | Details of the shipping address for this account. Postal code maximum size is 20 characters. |
| Shipping State | `shippingState` | string |  | Details of the shipping address for this account. State maximum size is 80 characters. |
| Shipping Street | `shippingStreet` | string |  | The street address of the shipping address for this account. Maximum of 255 characters. |
| Type Name or ID | `type` | options |  | Type of account. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Website | `website` | string |  | The website of this account. Maximum of 255 characters. |

</details>

| Case ID | `caseId` | string |  | ✓ | ID of case that needs to be fetched |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the account associated with this case | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account ID | `accountId` | string |  | ID of the account associated with this case |
| Contact ID | `contactId` | string |  | ID of the associated Contact |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Description | `description` | string |  | A text description of the case. Limit: 32 KB. |
| Is Escalated | `isEscalated` | boolean | False | Whether the case has been escalated (true) or not |
| Origin Name or ID | `origin` | options |  | The source of the case, such as Email, Phone, or Web. Label is Case Origin. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Owner Name or ID | `owner` | options |  | The owner of the case. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Parent ID | `ParentId` | string |  | The ID of the parent case in the hierarchy. The label is Parent Case. |
| Priority Name or ID | `priority` | options |  | The importance or urgency of the case, such as High, Medium, or Low. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Reason Name or ID | `reason` | options |  | The reason why the case was created, such as Instructions not clear, or User didn’t attend training. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Record Type Name or ID | `recordTypeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Status Name or ID | `status` | options |  | The status of the case, such as “New,” “Closed,” or “Escalated.” This field directly controls the IsClosed flag. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Subject | `subject` | string |  | The subject of the case. Limit: 255 characters. |
| Supplied Company | `suppliedCompany` | string |  | The company name that was entered when the case was created. This field can't be updated after the case has been created.. |
| Supplied Email | `suppliedEmail` | string |  | The email address that was entered when the case was created. This field can't be updated after the case has been created. |
| Supplied Name | `suppliedName` | string |  | The name that was entered when the case was created. This field can't be updated after the case has been created. |
| Supplied Phone | `suppliedPhone` | string |  | The phone number that was entered when the case was created. This field can't be updated after the case has been created. |
| Type Name or ID | `type` | options |  | The type of case. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Task ID | `taskId` | string |  | ✓ | ID of task that needs to be fetched |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Represents the due date of the task. This field has a timestamp that is always set to midnight in the Coordinated Universal Time (UTC) time zone. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Activity Date | `activityDate` | dateTime |  | Represents the due date of the task. This field has a timestamp that is always set to midnight in the Coordinated Universal Time (UTC) time zone. |
| Call Disposition | `callDisposition` | string |  | Represents the result of a given call, for example, “we'll call back,” or “call unsuccessful.” Limit is 255 characters. Not subject to field-level security, available for any user in an organization with Salesforce CRM Call Center. |
| Call Duration In Seconds | `callDurationInSeconds` | number |  | Duration of the call in seconds. Not subject to field-level security, available for any user in an organization with Salesforce CRM Call Center. |
| Call Object | `callObject` | string |  | Name of a call center. Limit is 255 characters. Not subject to field-level security, available for any user in an organization with Salesforce CRM Call Center. |
| Call Type Name or ID | `callType` | options |  | The type of call being answered: Inbound, Internal, or Outbound. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Custom Fields | `customFieldsUi` | fixedCollection | {} | Filter by custom fields |
| Description | `description` | string |  | Contains a text description of the task |
| Is ReminderSet | `isReminderSet` | boolean | False | Whether a popup reminder has been set for the task (true) or not (false) |
| Owner Name or ID | `owner` | options |  | ID of the User who owns the record. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Priority Name or ID | `priority` | options |  | Indicates the importance or urgency of a task, such as high or low. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Status Name or ID | `status` | options |  | The current status of the task, such as In Progress or Completed. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Subject Name or ID | `subject` | options |  | The subject line of the task, such as “Call” or “Send Quote.” Limit: 255 characters. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Recurrence Day Of Month | `recurrenceDayOfMonth` | number |  | The day of the month in which the task repeats |
| Recurrence Day Of Week Mask | `recurrenceDayOfWeekMask` | number |  | The day or days of the week on which the task repeats. This field contains a bitmask. The values are as follows: Sunday = 1 Monday = 2 Tuesday = 4 Wednesday = 8 Thursday = 16 Friday = 32 Saturday = 64. Multiple days are represented as the sum of their numerical values. For example, Tuesday and Thursday = 4 + 16 = 20. |
| Recurrence End Date Only | `recurrenceEndDateOnly` | dateTime |  | The last date on which the task repeats. This field has a timestamp that is always set to midnight in the Coordinated Universal Time (UTC) time zone. |
| Recurrence Instance Name or ID | `recurrenceInstance` | options |  | The frequency of the recurring task. For example, “2nd” or “3rd.”. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Recurrence Interval | `recurrenceInterval` | number |  | The interval between recurring tasks |
| Recurrence Month Of Year | `recurrenceMonthOfYear` | options |  | The month of the year in which the task repeats |
| Recurrence Start Date Only | `recurrenceEndDateOnly` | dateTime |  | The date when the recurring task begins. Must be a date and time before RecurrenceEndDateOnly. |
| Recurrence Regenerated Type | `recurrenceRegeneratedType` | options |  | Represents what triggers a repeating task to repeat. Add this field to a page layout together with the RecurrenceInterval field, which determines the number of days between the triggering date (due date or close date) and the due date of the next repeating task in the series. Label is Repeat This Task. |
| Recurrence Type Name or ID | `recurrenceType` | options |  | Website for the task. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Recurrence TimeZone SidKey | `recurrenceTimeZoneSidKey` | string |  | The time zone associated with the recurring task. For example, “UTC-8:00” for Pacific Standard Time. |
| Reminder Date Time | `reminderDateTime` | dateTime |  | Represents the time when the reminder is scheduled to fire, if IsReminderSet is set to true. If IsReminderSet is set to false, then the user may have deselected the reminder checkbox in the Salesforce user interface, or the reminder has already fired at the time indicated by the value. |
| Type Name or ID | `type` | options |  | Represents Type of the task, such as Call or Meeting. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| What ID | `whatId` | string |  | The WhatId represents nonhuman objects such as accounts, opportunities, campaigns, cases, or custom objects. WhatIds are polymorphic. Polymorphic means a WhatId is equivalent to the ID of a related object. |
| Who ID | `whoId` | string |  | The WhoId represents a human such as a lead or a contact. WhoIds are polymorphic. Polymorphic means a WhoId is equivalent to a contact’s ID or a lead’s ID. |

</details>

| Attachment ID | `attachmentId` | string |  | ✓ | ID of attachment that needs to be fetched |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Text description of the Document. Limit: 255 characters. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Input Binary Field | `binaryPropertyName` | string | data |  |
| Description | `description` | string |  | Text description of the Document. Limit: 255 characters. |
| Is Private | `isPrivate` | boolean | False | Whether this record is viewable only by the owner and administrators (true) or viewable by all otherwise-allowed users (false) |
| Name | `name` | string |  | Required. Name of the attached file. Maximum size is 255 characters. Label is File Name. |
| Owner Name or ID | `owner` | options |  | ID of the User who owns the attachment. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Upload parameters (`upload`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Title | `title` | string |  | ✓ | Name of the file |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be uploaded |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | File extension to use. If none is set, the value from the binary data will be used. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| File Extension | `fileExtension` | string |  | File extension to use. If none is set, the value from the binary data will be used. |
| Link To Object ID | `linkToObjectId` | string |  | ID of the object you want to link this document to |
| Owner Name or ID | `ownerId` | options |  | ID of the owner of this document. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Query parameters (`query`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Query | `query` | string |  | ✓ | A SOQL query. An example query parameter string might look like: “SELECT+Name+FROM+MyObject”. If the SOQL query string is invalid, a MALFORMED_QUERY response is returned. |  |

### Add Comment parameters (`addComment`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Case ID | `caseId` | string |  | ✓ | ID of case that needs to be fetched |  |
| Options | `options` | collection | {} | ✗ | Text of the CaseComment. The maximum size of the comment body is 4,000 bytes. Label is Body. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Comment Body | `commentBody` | string |  | Text of the CaseComment. The maximum size of the comment body is 4,000 bytes. Label is Body. |
| Is Published | `isPublished` | boolean | False | Whether the CaseComment is visible to customers in the Self-Service portal (true) or not (false) |

</details>


### Invoke parameters (`invoke`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| API Name | `apiName` | string |  | ✓ | Required. API name of the flow. |  |
| JSON Parameters | `jsonParameters` | boolean | False | ✗ | Whether the input variables should be set via the value-key pair UI or JSON/RAW |  |
| Variables | `variablesJson` | json |  | ✗ | Input variables as JSON object |  |
| Variables | `variablesUi` | fixedCollection | {} | ✗ | The input variable to send | e.g. Add Variable |  |

<details>
<summary><strong>Variables sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Variable | `variablesValues` |  |  |  |

</details>


---

## Load Options Methods

- `getLeadStatuses`
- `q`

---

## Real-World Examples

These examples are extracted from actual n8n workflows:

### Example 1: Salesforce

**From workflow:** tasks.workflow

**Parameters:**
```json
{
  "resource": "task",
  "status": "In Progress",
  "additionalFields": {
    "description": "Sample description",
    "subject": "Email"
  }
}
```

**Credentials:**
- salesforceOAuth2Api: `Salesforce account`

### Example 2: Salesforce1

**From workflow:** tasks.workflow

**Parameters:**
```json
{
  "resource": "task",
  "operation": "getAll",
  "returnAll": true,
  "options": {}
}
```

**Credentials:**
- salesforceOAuth2Api: `Salesforce account`

### Example 3: Salesforce2

**From workflow:** tasks.workflow

**Parameters:**
```json
{
  "resource": "task",
  "operation": "get",
  "taskId": "id1"
}
```

**Credentials:**
- salesforceOAuth2Api: `Salesforce account`

### Example 4: Salesforce3

**From workflow:** tasks.workflow

**Parameters:**
```json
{
  "resource": "task",
  "operation": "getSummary"
}
```

**Credentials:**
- salesforceOAuth2Api: `Salesforce account`

### Example 5: Salesforce4

**From workflow:** tasks.workflow

**Parameters:**
```json
{
  "resource": "task",
  "operation": "update",
  "taskId": "id1",
  "updateFields": {
    "description": "New description"
  }
}
```

**Credentials:**
- salesforceOAuth2Api: `Salesforce account`


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
* Categories: Sales, Communication

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: salesforce
displayName: Salesforce
description: Consume Salesforce API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: salesforceOAuth2Api
  required: true
- name: salesforceJwtApi
  required: true
operations:
- id: addToCampaign
  name: Add Lead To Campaign
  description: Add lead to a campaign
  params:
  - id: leadId
    name: Lead ID
    type: string
    default: ''
    required: true
    description: ID of contact that needs to be fetched
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - lead
          operation:
          - addNote
    typeInfo: &id004
      type: string
      displayName: Lead ID
      name: leadId
  - id: campaignId
    name: Campaign Name or ID
    type: options
    default: ''
    required: true
    description: ID of the campaign that needs to be fetched. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - addToCampaign
    typeInfo: &id002
      type: options
      displayName: Campaign Name or ID
      name: campaignId
      typeOptions:
        loadOptionsMethod: getCampaigns
      possibleValues: []
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of contact that needs to be fetched
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - addNote
    typeInfo: &id006
      type: string
      displayName: Contact ID
      name: contactId
  - id: campaignId
    name: Campaign Name or ID
    type: options
    default: ''
    required: true
    description: ID of the campaign that needs to be fetched. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
- id: addNote
  name: Add Note
  description: Add note to a lead
  params:
  - id: leadId
    name: Lead ID
    type: string
    default: ''
    required: true
    description: ID of lead that needs to be fetched
    validation: *id003
    typeInfo: *id004
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the note
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - account
          operation:
          - addNote
    typeInfo: &id008
      type: string
      displayName: Title
      name: title
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of contact that needs to be fetched
    validation: *id005
    typeInfo: *id006
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the note
    validation: *id007
    typeInfo: *id008
  - id: opportunityId
    name: Opportunity ID
    type: string
    default: ''
    required: true
    description: ID of opportunity that needs to be fetched
    validation: &id028
      required: true
      displayOptions:
        show:
          resource:
          - opportunity
          operation:
          - addNote
    typeInfo: &id029
      type: string
      displayName: Opportunity ID
      name: opportunityId
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the note
    validation: *id007
    typeInfo: *id008
  - id: accountId
    name: Account ID
    type: string
    default: ''
    required: true
    description: ID of account that needs to be fetched
    validation: &id030
      required: true
      displayOptions:
        show:
          resource:
          - account
          operation:
          - addNote
    typeInfo: &id031
      type: string
      displayName: Account ID
      name: accountId
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Title of the note
    validation: *id007
    typeInfo: *id008
- id: create
  name: Create
  description: Create a lead
  params:
  - id: company
    name: Company
    type: string
    default: ''
    required: true
    description: Company of the lead. If person account record types have been enabled,
      and if the value of Company is null, the lead converts to a person account.
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - lead
          operation:
          - create
          - upsert
    typeInfo: &id014
      type: string
      displayName: Company
      name: company
  - id: lastname
    name: Last Name
    type: string
    default: ''
    required: true
    description: Required. Last name of the lead. Limited to 80 characters.
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - create
          - upsert
    typeInfo: &id010
      type: string
      displayName: Last Name
      name: lastname
  - id: lastname
    name: Last Name
    type: string
    default: ''
    required: true
    description: Required. Last name of the contact. Limited to 80 characters.
    validation: *id009
    typeInfo: *id010
  - id: customObject
    name: Custom Object Name or ID
    type: options
    default: ''
    required: true
    description: Name of the custom object. Choose from the list, or specify an ID
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id019
      required: true
      displayOptions:
        show:
          resource:
          - customObject
          operation:
          - getAll
    typeInfo: &id020
      type: options
      displayName: Custom Object Name or ID
      name: customObject
      typeOptions:
        loadOptionsMethod: getCustomObjects
      possibleValues: []
  - id: customFieldsUi
    name: Fields
    type: fixedCollection
    default: &id021 {}
    required: false
    description: Filter by custom fields
    placeholder: Add Field
    validation: &id022
      displayOptions:
        show:
          resource:
          - customObject
          operation:
          - update
    typeInfo: &id023
      type: fixedCollection
      displayName: Fields
      name: customFieldsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: customFieldsValues
        displayName: Custom Field
        values:
        - displayName: Field Name or ID
          name: fieldId
          type: options
          description: The ID of the field. Choose from the list, or specify an ID
            using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
          default: ''
          typeOptions:
            loadOptionsMethod: getCustomObjectFields
        - displayName: Value
          name: value
          type: string
          description: The value to set on custom field
          default: ''
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Required. Last name of the opportunity. Limited to 80 characters.
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - attachment
          operation:
          - create
    typeInfo: &id012
      type: string
      displayName: Name
      name: name
  - id: closeDate
    name: Close Date
    type: dateTime
    default: ''
    required: true
    description: Required. Date when the opportunity is expected to close.
    validation: &id024
      required: true
      displayOptions:
        show:
          resource:
          - opportunity
          operation:
          - create
          - upsert
    typeInfo: &id025
      type: dateTime
      displayName: Close Date
      name: closeDate
  - id: stageName
    name: Stage Name or ID
    type: options
    default: ''
    required: true
    description: Required. Date when the opportunity is expected to close. Choose
      from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id026
      required: true
      displayOptions:
        show:
          resource:
          - opportunity
          operation:
          - create
          - upsert
    typeInfo: &id027
      type: options
      displayName: Stage Name or ID
      name: stageName
      typeOptions:
        loadOptionsMethod: getStages
      possibleValues: []
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the account. Maximum size is 255 characters.
    validation: *id011
    typeInfo: *id012
  - id: type
    name: Type Name or ID
    type: options
    default: ''
    required: true
    description: The type of case. Choose from the list, or specify an ID using an
      <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - case
          operation:
          - create
    typeInfo:
      type: options
      displayName: Type Name or ID
      name: type
      typeOptions:
        loadOptionsMethod: getCaseTypes
      possibleValues: []
  - id: status
    name: Status Name or ID
    type: options
    default: ''
    required: true
    description: The current status of the task, such as In Progress or Completed.
      Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - create
    typeInfo:
      type: options
      displayName: Status Name or ID
      name: status
      typeOptions:
        loadOptionsMethod: getTaskStatuses
      possibleValues: []
  - id: parentId
    name: Parent ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - attachment
          operation:
          - create
    typeInfo:
      type: string
      displayName: Parent ID
      name: parentId
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Required. Name of the attached file. Maximum size is 255 characters.
      Label is File Name.
    validation: *id011
    typeInfo: *id012
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be uploaded
    validation: &id044
      required: true
      displayOptions:
        show:
          resource:
          - attachment
          operation:
          - create
    typeInfo: &id045
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
- id: upsert
  name: Create or Update
  description: Create a new lead, or update the current one if it already exists (upsert)
  params:
  - id: externalId
    name: Match Against
    type: options
    default: ''
    required: true
    description: The field to check to see if the lead already exists. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - account
          operation:
          - upsert
    typeInfo: &id016
      type: options
      displayName: Match Against
      name: externalId
      typeOptions:
        loadOptionsMethod: getExternalIdFields
      possibleValues: []
  - id: externalIdValue
    name: Value to Match
    type: string
    default: ''
    required: true
    description: If this value exists in the 'match against' field, update the lead.
      Otherwise create a new one.
    validation: &id017
      required: true
      displayOptions:
        show:
          resource:
          - account
          operation:
          - upsert
    typeInfo: &id018
      type: string
      displayName: Value to Match
      name: externalIdValue
  - id: company
    name: Company
    type: string
    default: ''
    required: true
    description: Company of the lead. If person account record types have been enabled,
      and if the value of Company is null, the lead converts to a person account.
    validation: *id013
    typeInfo: *id014
  - id: lastname
    name: Last Name
    type: string
    default: ''
    required: true
    description: Required. Last name of the lead. Limited to 80 characters.
    validation: *id009
    typeInfo: *id010
  - id: externalId
    name: Match Against
    type: options
    default: ''
    required: true
    description: The field to check to see if the contact already exists. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id015
    typeInfo: *id016
  - id: externalIdValue
    name: Value to Match
    type: string
    default: ''
    required: true
    description: If this value exists in the 'match against' field, update the contact.
      Otherwise create a new one.
    validation: *id017
    typeInfo: *id018
  - id: lastname
    name: Last Name
    type: string
    default: ''
    required: true
    description: Required. Last name of the contact. Limited to 80 characters.
    validation: *id009
    typeInfo: *id010
  - id: customObject
    name: Custom Object Name or ID
    type: options
    default: ''
    required: true
    description: Name of the custom object. Choose from the list, or specify an ID
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id019
    typeInfo: *id020
  - id: externalId
    name: Match Against
    type: options
    default: ''
    required: true
    description: The field to check to see if the object already exists. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id015
    typeInfo: *id016
  - id: externalIdValue
    name: Value to Match
    type: string
    default: ''
    required: true
    description: If this value exists in the 'match against' field, update the object.
      Otherwise create a new one.
    validation: *id017
    typeInfo: *id018
  - id: customFieldsUi
    name: Fields
    type: fixedCollection
    default: *id021
    required: false
    description: Filter by custom fields
    placeholder: Add Field
    validation: *id022
    typeInfo: *id023
  - id: externalId
    name: Match Against
    type: options
    default: ''
    required: true
    description: The field to check to see if the opportunity already exists. Choose
      from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id015
    typeInfo: *id016
  - id: externalIdValue
    name: Value to Match
    type: string
    default: ''
    required: true
    description: If this value exists in the 'match against' field, update the opportunity.
      Otherwise create a new one.
    validation: *id017
    typeInfo: *id018
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Required. Last name of the opportunity. Limited to 80 characters.
    validation: *id011
    typeInfo: *id012
  - id: closeDate
    name: Close Date
    type: dateTime
    default: ''
    required: true
    description: Required. Date when the opportunity is expected to close.
    validation: *id024
    typeInfo: *id025
  - id: stageName
    name: Stage Name or ID
    type: options
    default: ''
    required: true
    description: Required. Date when the opportunity is expected to close. Choose
      from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id026
    typeInfo: *id027
  - id: externalId
    name: Match Against
    type: options
    default: ''
    required: true
    description: The field to check to see if the account already exists. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id015
    typeInfo: *id016
  - id: externalIdValue
    name: Value to Match
    type: string
    default: ''
    required: true
    description: If this value exists in the 'match against' field, update the account.
      Otherwise create a new one.
    validation: *id017
    typeInfo: *id018
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the account. Maximum size is 255 characters.
    validation: *id011
    typeInfo: *id012
- id: delete
  name: Delete
  description: Delete a lead
  params:
  - id: leadId
    name: Lead ID
    type: string
    default: ''
    required: true
    description: ID of Lead that needs to be fetched
    validation: *id003
    typeInfo: *id004
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of contact that needs to be fetched
    validation: *id005
    typeInfo: *id006
  - id: customObject
    name: Custom Object Name or ID
    type: options
    default: ''
    required: true
    description: Name of the custom object. Choose from the list, or specify an ID
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id019
    typeInfo: *id020
  - id: recordId
    name: Record ID
    type: string
    default: ''
    required: true
    description: Record ID to be deleted
    validation: &id032
      required: true
      displayOptions:
        show:
          resource:
          - customObject
          operation:
          - delete
    typeInfo: &id033
      type: string
      displayName: Record ID
      name: recordId
  - id: opportunityId
    name: Opportunity ID
    type: string
    default: ''
    required: true
    description: ID of opportunity that needs to be fetched
    validation: *id028
    typeInfo: *id029
  - id: accountId
    name: Account ID
    type: string
    default: ''
    required: true
    description: ID of account that needs to be fetched
    validation: *id030
    typeInfo: *id031
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ID of case that needs to be fetched
    validation: &id034
      required: true
      displayOptions:
        show:
          resource:
          - case
          operation:
          - addComment
    typeInfo: &id035
      type: string
      displayName: Case ID
      name: caseId
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of task that needs to be fetched
    validation: &id036
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - delete
    typeInfo: &id037
      type: string
      displayName: Task ID
      name: taskId
  - id: attachmentId
    name: Attachment ID
    type: string
    default: ''
    required: true
    description: ID of attachment that needs to be fetched
    validation: &id038
      required: true
      displayOptions:
        show:
          resource:
          - attachment
          operation:
          - delete
    typeInfo: &id039
      type: string
      displayName: Attachment ID
      name: attachmentId
- id: get
  name: Get
  description: Get a lead
  params:
  - id: leadId
    name: Lead ID
    type: string
    default: ''
    required: true
    description: ID of Lead that needs to be fetched
    validation: *id003
    typeInfo: *id004
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of contact that needs to be fetched
    validation: *id005
    typeInfo: *id006
  - id: customObject
    name: Custom Object Name or ID
    type: options
    default: ''
    required: true
    description: Name of the custom object. Choose from the list, or specify an ID
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id019
    typeInfo: *id020
  - id: recordId
    name: Record ID
    type: string
    default: ''
    required: true
    description: Record ID to be retrieved
    validation: *id032
    typeInfo: *id033
  - id: opportunityId
    name: Opportunity ID
    type: string
    default: ''
    required: true
    description: ID of opportunity that needs to be fetched
    validation: *id028
    typeInfo: *id029
  - id: accountId
    name: Account ID
    type: string
    default: ''
    required: true
    description: ID of account that needs to be fetched
    validation: *id030
    typeInfo: *id031
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ID of case that needs to be fetched
    validation: *id034
    typeInfo: *id035
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of task that needs to be fetched
    validation: *id036
    typeInfo: *id037
  - id: attachmentId
    name: Attachment ID
    type: string
    default: ''
    required: true
    description: ID of attachment that needs to be fetched
    validation: *id038
    typeInfo: *id039
  - id: userId
    name: User ID
    type: string
    default: ''
    required: true
    description: ID of user that needs to be fetched
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - user
          operation:
          - get
    typeInfo:
      type: string
      displayName: User ID
      name: userId
- id: getAll
  name: Get Many
  description: Get many leads
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id040
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - flow
    typeInfo: &id041
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id042
      displayOptions:
        show:
          operation:
          - getAll
          resource:
          - flow
          returnAll:
          - false
    typeInfo: &id043
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 500
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id040
    typeInfo: *id041
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id042
    typeInfo: *id043
  - id: customObject
    name: Custom Object Name or ID
    type: options
    default: ''
    required: true
    description: Name of the custom object. Choose from the list, or specify an ID
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id019
    typeInfo: *id020
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id040
    typeInfo: *id041
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id042
    typeInfo: *id043
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id040
    typeInfo: *id041
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id042
    typeInfo: *id043
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id040
    typeInfo: *id041
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id042
    typeInfo: *id043
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id040
    typeInfo: *id041
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id042
    typeInfo: *id043
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id040
    typeInfo: *id041
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id042
    typeInfo: *id043
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id040
    typeInfo: *id041
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id042
    typeInfo: *id043
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id040
    typeInfo: *id041
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id042
    typeInfo: *id043
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id040
    typeInfo: *id041
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id042
    typeInfo: *id043
- id: getSummary
  name: Get Summary
  description: Returns an overview of Lead's metadata
- id: update
  name: Update
  description: Update a lead
  params:
  - id: leadId
    name: Lead ID
    type: string
    default: ''
    required: true
    description: ID of Lead that needs to be fetched
    validation: *id003
    typeInfo: *id004
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of contact that needs to be fetched
    validation: *id005
    typeInfo: *id006
  - id: customObject
    name: Custom Object Name or ID
    type: options
    default: ''
    required: true
    description: Name of the custom object. Choose from the list, or specify an ID
      using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id019
    typeInfo: *id020
  - id: recordId
    name: Record ID
    type: string
    default: ''
    required: true
    description: Record ID to be updated
    validation: *id032
    typeInfo: *id033
  - id: customFieldsUi
    name: Fields
    type: fixedCollection
    default: {}
    required: false
    description: Filter by custom fields
    placeholder: Add Field
    validation: *id022
    typeInfo: *id023
  - id: opportunityId
    name: Opportunity ID
    type: string
    default: ''
    required: true
    description: ID of opportunity that needs to be fetched
    validation: *id028
    typeInfo: *id029
  - id: accountId
    name: Account ID
    type: string
    default: ''
    required: true
    description: ID of account that needs to be fetched
    validation: *id030
    typeInfo: *id031
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ID of case that needs to be fetched
    validation: *id034
    typeInfo: *id035
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ID of task that needs to be fetched
    validation: *id036
    typeInfo: *id037
  - id: attachmentId
    name: Attachment ID
    type: string
    default: ''
    required: true
    description: ID of attachment that needs to be fetched
    validation: *id038
    typeInfo: *id039
- id: upload
  name: Upload
  description: Upload a document
  params:
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: Name of the file
    validation: *id007
    typeInfo: *id008
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be uploaded
    validation: *id044
    typeInfo: *id045
- id: query
  name: Query
  description: Execute a SOQL query that returns all the results in a single response
  params:
  - id: query
    name: Query
    type: string
    default: ''
    required: true
    description: 'A SOQL query. An example query parameter string might look like:
      “SELECT+Name+FROM+MyObject”. If the SOQL query string is invalid, a MALFORMED_QUERY
      response is returned.'
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
      displayName: Query
      name: query
- id: addComment
  name: Add Comment
  description: Add a comment to a case
  params:
  - id: caseId
    name: Case ID
    type: string
    default: ''
    required: true
    description: ID of case that needs to be fetched
    validation: *id034
    typeInfo: *id035
- id: invoke
  name: Invoke
  description: Invoke a flow
  params:
  - id: apiName
    name: API Name
    type: string
    default: ''
    required: true
    description: Required. API name of the flow.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - flow
          operation:
          - invoke
    typeInfo:
      type: string
      displayName: API Name
      name: apiName
  - id: jsonParameters
    name: JSON Parameters
    type: boolean
    default: false
    required: false
    description: Whether the input variables should be set via the value-key pair
      UI or JSON/RAW
    validation:
      displayOptions:
        show:
          resource:
          - flow
          operation:
          - invoke
    typeInfo:
      type: boolean
      displayName: JSON Parameters
      name: jsonParameters
  - id: variablesJson
    name: Variables
    type: json
    default: ''
    required: false
    description: Input variables as JSON object
    validation:
      displayOptions:
        show:
          resource:
          - flow
          operation:
          - invoke
          jsonParameters:
          - true
    typeInfo:
      type: json
      displayName: Variables
      name: variablesJson
  - id: variablesUi
    name: Variables
    type: fixedCollection
    default: {}
    required: false
    description: The input variable to send
    placeholder: Add Variable
    validation:
      displayOptions:
        show:
          resource:
          - flow
          operation:
          - invoke
          jsonParameters:
          - false
    typeInfo:
      type: fixedCollection
      displayName: Variables
      name: variablesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: variablesValues
        displayName: Variable
        values:
        - displayName: Name
          name: name
          type: string
          description: Name of the input variable
          default: ''
        - displayName: Value
          name: value
          type: string
          description: Value of the input variable
          default: ''
examples:
- name: Salesforce
  parameters:
    resource: task
    status: In Progress
    additionalFields:
      description: Sample description
      subject: Email
  workflow: tasks.workflow
- name: Salesforce1
  parameters:
    resource: task
    operation: getAll
    returnAll: true
    options: {}
  workflow: tasks.workflow
- name: Salesforce2
  parameters:
    resource: task
    operation: get
    taskId: id1
  workflow: tasks.workflow
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods:
  - POST
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
  - field: updateFields
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: customFieldsUi
    text: Add Field
  - field: customFieldsUi
    text: Add Field
  - field: options
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
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: options
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: variablesUi
    text: Add Variable
  hints:
  - field: binaryPropertyName
    text: The name of the input binary field containing the file to be uploaded
  - field: binaryPropertyName
    text: The name of the input binary field containing the file to be uploaded
  - field: updateFields
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
  "$id": "https://n8n.io/schemas/nodes/salesforce.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Salesforce Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "addToCampaign",
        "addNote",
        "create",
        "upsert",
        "delete",
        "get",
        "getAll",
        "getSummary",
        "update",
        "upload",
        "query",
        "addComment",
        "invoke"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "authentication": {
          "description": "OAuth Authorization Flow",
          "type": "string",
          "enum": [
            "oAuth2",
            "jwt"
          ],
          "default": "oAuth2"
        },
        "resource": {
          "description": "Represents an individual account, which is an organization or person involved with your business (such as customers, competitors, and partners)",
          "type": "string",
          "enum": [
            "account",
            "attachment",
            "case",
            "contact",
            "customObject",
            "document",
            "flow",
            "lead",
            "opportunity",
            "search",
            "task",
            "user"
          ],
          "default": "lead"
        },
        "operation": {
          "description": "Get many flows",
          "type": "string",
          "enum": [
            "getAll",
            "invoke"
          ],
          "default": "invoke"
        },
        "externalId": {
          "description": "The field to check to see if the account already exists. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "externalIdValue": {
          "description": "If this value exists in the 'match against' field, update the account. Otherwise create a new one.",
          "type": "string",
          "default": ""
        },
        "company": {
          "description": "Company of the lead. If person account record types have been enabled, and if the value of Company is null, the lead converts to a person account.",
          "type": "string",
          "default": ""
        },
        "lastname": {
          "description": "Required. Last name of the contact. Limited to 80 characters.",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Text description of the Document. Limit: 255 characters.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "leadId": {
          "description": "ID of lead that needs to be fetched",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "Text description of the Document. Limit: 255 characters.",
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
        "options": {
          "description": "The condition to set",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "campaignId": {
          "description": "ID of the campaign that needs to be fetched. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "title": {
          "description": "Title of the note",
          "type": "string",
          "default": ""
        },
        "contactId": {
          "description": "ID of contact that needs to be fetched",
          "type": "string",
          "default": ""
        },
        "customObject": {
          "description": "Name of the custom object. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "customFieldsUi": {
          "description": "Filter by custom fields",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "recordId": {
          "description": "Record ID to be deleted",
          "type": "string",
          "default": ""
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "name": {
          "description": "Required. Name of the attached file. Maximum size is 255 characters. Label is File Name.",
          "type": "string",
          "default": ""
        },
        "closeDate": {
          "description": "Required. Date when the opportunity is expected to close.",
          "type": "string",
          "default": ""
        },
        "stageName": {
          "description": "Required. Date when the opportunity is expected to close. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "opportunityId": {
          "description": "ID of opportunity that needs to be fetched",
          "type": "string",
          "default": ""
        },
        "accountId": {
          "description": "ID of account that needs to be fetched",
          "type": "string",
          "default": ""
        },
        "query": {
          "description": "A SOQL query. An example query parameter string might look like: \u201cSELECT+Name+FROM+MyObject\u201d. If the SOQL query string is invalid, a MALFORMED_QUERY response is returned.",
          "type": "string",
          "default": ""
        },
        "type": {
          "description": "The type of case. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "caseId": {
          "description": "ID of case that needs to be fetched",
          "type": "string",
          "default": ""
        },
        "status": {
          "description": "The current status of the task, such as In Progress or Completed. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "taskId": {
          "description": "ID of task that needs to be fetched",
          "type": "string",
          "default": ""
        },
        "parentId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "attachmentId": {
          "description": "ID of attachment that needs to be fetched",
          "type": "string",
          "default": ""
        },
        "userId": {
          "description": "ID of user that needs to be fetched",
          "type": "string",
          "default": ""
        },
        "apiName": {
          "description": "Required. API name of the flow.",
          "type": "string",
          "default": ""
        },
        "jsonParameters": {
          "description": "Whether the input variables should be set via the value-key pair UI or JSON/RAW",
          "type": "boolean",
          "default": false
        },
        "variablesJson": {
          "description": "Input variables as JSON object",
          "type": "string",
          "default": ""
        },
        "variablesUi": {
          "description": "The input variable to send",
          "type": "string",
          "default": {},
          "examples": [
            "Add Variable"
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
      "name": "salesforceOAuth2Api",
      "required": true
    },
    {
      "name": "salesforceJwtApi",
      "required": true
    }
  ],
  "examples": [
    {
      "description": "Salesforce",
      "value": {
        "resource": "task",
        "status": "In Progress",
        "additionalFields": {
          "description": "Sample description",
          "subject": "Email"
        }
      }
    },
    {
      "description": "Salesforce1",
      "value": {
        "resource": "task",
        "operation": "getAll",
        "returnAll": true,
        "options": {}
      }
    },
    {
      "description": "Salesforce2",
      "value": {
        "resource": "task",
        "operation": "get",
        "taskId": "id1"
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
