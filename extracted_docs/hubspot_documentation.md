---
title: "Node: HubSpot"
slug: "node-hubspot"
version: "['2', '2.1', '2.2']"
updated: "2026-01-08"
summary: "Consume HubSpot API"
node_type: "regular"
group: "['output']"
---

# Node: HubSpot

**Purpose.** Consume HubSpot API
**Subtitle.** ={{$parameter[


---

## Node Details

- **Icon:** `file:hubspot.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **hubspotApi**: N/A
- **hubspotAppToken**: N/A
- **hubspotOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `hubspotApi` | ✓ | {'show': {'authentication': ['apiKey']}} |
| `hubspotAppToken` | ✓ | {'show': {'authentication': ['appToken']}} |
| `hubspotOAuth2Api` | ✓ | {'show': {'authentication': ['oAuth2']}} |

---

## API Patterns

**HTTP Methods:** GET

---

## Operations

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create or Update | `upsert` | Create a new contact, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a contact |
| Get | `get` | Get a contact |
| Get Many | `getAll` | Get many contacts |
| Get Recently Created/Updated | `getRecentlyCreatedUpdated` | Get recently created/updated contacts |
| Search | `search` | Search contacts |

### Contactlist Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add contact to a list |
| Remove | `remove` | Remove a contact from a list |

### Company Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a company |
| Delete | `delete` | Delete a company |
| Get | `get` | Get a company |
| Get Many | `getAll` | Get many companies |
| Get Recently Created/Updated | `getRecentlyCreatedUpdated` | Get recently created/updated companies |
| Search | `searchByDomain` | Search companies by their website domain |
| Update | `update` | Update a company |

### Deal Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a deal |
| Delete | `delete` | Delete a deal |
| Get | `get` | Get a deal |
| Get Many | `getAll` | Get many deals |
| Get Recently Created/Updated | `getRecentlyCreatedUpdated` | Get recently created/updated deals |
| Search | `search` | Search deals |
| Update | `update` | Update a deal |

### Engagement Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an engagement |
| Delete | `delete` | Delete an engagement |
| Get | `get` | Get an engagement |
| Get Many | `getAll` | Get many engagements |

### Ticket Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a ticket |
| Delete | `delete` | Delete a ticket |
| Get | `get` | Get a ticket |
| Get Many | `getAll` | Get many tickets |
| Update | `update` | Update a ticket |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | contact | ✗ | Resource to operate on |  |

**Resource options:**

* **Company** (`company`)
* **Contact** (`contact`)
* **Contact List** (`contactList`)
* **Deal** (`deal`)
* **Engagement** (`engagement`)
* **Form** (`form`)
* **Ticket** (`ticket`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | upsert | ✗ | Create a new contact, or update the current one if it already exists (upsert) |  |

**Operation options:**

* **Create or Update** (`upsert`) - Create a new contact, or update the current one if it already exists (upsert)
* **Delete** (`delete`) - Delete a contact
* **Get** (`get`) - Get a contact
* **Get Many** (`getAll`) - Get many contacts
* **Get Recently Created/Updated** (`getRecentlyCreatedUpdated`) - Get recently created/updated contacts
* **Search** (`search`) - Search contacts

---

### Create or Update parameters (`upsert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Email | `email` | string |  | ✓ | e.g. name@email.com | email |
| Contact Properties | `additionalFields` | collection | {} | ✓ | Companies associated with the ticket. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Property | min:0, max:∞ |

<details>
<summary><strong>Contact Properties sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Annual Revenue | `annualRevenue` | number | 0 |  |
| Associated Company Name or ID | `associatedCompanyId` | options |  | Companies associated with the ticket. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Buying Role | `buyingRole` | multiOptions | [] | Role the contact plays during the sales process. Contacts can have multiple roles, and can share roles with others. |
| City | `city` | string |  |  |
| Clicked Facebook Ad | `clickedFacebookAd` | string |  |  |
| Close Date | `closeDate` | dateTime |  | When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format |
| Company Name | `companyName` | string |  |  |
| Company Size | `companySize` | string |  |  |
| Contact Owner Name or ID | `contactOwner` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Contact Properties to Include | `properties` | multiOptions | [] | Whether to include specific Contact properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Country/Region | `country` | string |  |  |
| Country/Region Code | `countryRegionCode` | string |  | The contact's two-letter country code |
| Custom Properties | `customPropertiesUi` | fixedCollection | {} | Name of the property. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Date of Birth | `dateOfBirth` | dateTime |  | When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format |
| Degree | `degree` | string |  |  |
| Email Address Quarantine Reason | `emailCustomerQuarantinedReason` | options |  | The reason why the email address has been quarantined |
| Employment Role | `employmentRole` | options |  | Job role |
| Employment Seniority | `employmentSeniority` | options |  | Job Seniority |
| Employment Sub Role | `employmentSubRole` | options |  | Job sub role |
| Enriched Email Bounce Detected | `enrichedEmailBounceDetected` | boolean | False |  |
| Facebook Click ID | `facebookClickId` | number |  |  |
| Fax Number | `faxNumber` | string |  |  |
| Field Of Study | `fieldOfStudy` | string |  | A contact's field of study. This property is required for the Facebook Ads Integration. This property will be automatically synced via the Lead Ads tool |
| First Name | `firstName` | string |  | A contact's first name |
| Gender | `gender` | string |  |  |
| Google Ad Click ID | `googleAdClickId` | number |  |  |
| Graduation Date | `graduationDate` | dateTime |  | A contact's graduation date. This property is required for the Facebook Ads Integration. This property will be automatically synced via the Lead Ads tool. When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format |
| Industry | `industry` | string |  | The industry a contact is in |
| Inferred Language Codes | `inferredLanguageCodes` | options |  | Inferred languages based on location. ISO 639-1. |
| Job Function | `jobFunction` | string |  | A contact's job function. This property is required for the Facebook Ads Integration. This property will be automatically synced via the Lead Ads tool |
| Job Title | `jobTitle` | string |  | A contact's job title |
| Last Name | `lastName` | string |  | A contact's last name |
| Latest Traffic Source | `latestTrafficSource` | options |  | The source of the latest session for a contact |
| Latest Traffic Source Date | `latestTrafficSourceDate` | dateTime |  | The time of the latest session for a contact |
| Lead Status Name or ID | `leadStatus` | options |  | The contact's sales, prospecting or outreach status. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Legal Basic For Processing Contact Data Name or ID | `processingContactData` | options |  | Legal basis for processing contact's data; 'Not applicable' will exempt the contact from GDPR protections. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Lifecycle Stage Name or ID | `lifeCycleStage` | options |  | The qualification of contacts to sales readiness. It can be set through imports, forms, workflows, and manually on a per contact basis. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| LinkedIn URL | `linkedinUrl` | string |  | The URL of the contact's LinkedIn page |
| Marital Status | `maritalStatus` | string |  | A contact's marital status. This property is required for the Facebook Ads Integration. This property will be automatically synced via the Lead Ads tool |
| Member Email | `memberEmail` | string |  | Email used to send private content information to members |
| Membership Note | `membershipNote` | string |  | The notes relating to the contact's content membership |
| Message | `message` | string |  | A default property to be used for any message or comments a contact may want to leave on a form |
| Military Status | `militaryStatus` | string |  | Contact's military status. Required for the Facebook Ads Integration. Automatically synced from the Lead Ads tool. |
| Mobile Phone Number | `mobilePhoneNumber` | string |  | A contact's mobile phone number |
| Number Of Employees | `numberOfEmployees` | options |  | The number of company employees. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Original Source Name or ID | `originalSource` | options |  | The first known source through which a contact found your website. Source is automatically set by HubSpot, but may be updated manually. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Persona | `persona` | string |  | A contact's persona |
| Phone Number | `phoneNumber` | string |  | A contact's primary phone number |
| Postal Code | `postalCode` | string |  | The contact's zip code. This might be set via import, form, or integration. |
| Preffered Language Name or ID | `prefferedLanguage` | options |  | Set your contact's preferred language for communications. This property can be changed from an import, form, or integration. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Prospecting Agent Last Enrolled | `prospectingAgentLastEnrolled` | dateTime |  | The last time the Prospecting Agent enrolled this contact |
| Prospecting Agent Total Enrolled Count | `prospectingAgentTotalEnrolledCount` | number |  |  |
| Relationship Status | `relationshipStatus` | string |  | A contact's relationship status. This property is required for the Facebook Ads Integration. This property will be automatically synced via the Lead Ads tool |
| Salutation | `salutation` | string |  | The title used to address a contact |
| School | `school` | string |  | A contact's school. This property is required for the Facebook Ads Integration. This property will be automatically synced via the Lead Ads tool |
| Seniority | `seniority` | string |  | A contact's seniority. This property is required for the Facebook Ads Integration. This property will be automatically synced via the Lead Ads tool |
| Start Date | `startDate` | dateTime |  | A contact's start date. This property is required for the Facebook Ads Integration. This property will be automatically synced via the Lead Ads tool. When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format |
| State/Region | `stateRegion` | string |  | The contact's state of residence. This might be set via import, form, or integration. |
| State/Region Code | `stateRegionCode` | string |  | The contact's state or region code |
| Status Name or ID | `status` | options |  | The status of the contact's content membership. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Street Address | `streetAddress` | string |  | A contact's street address, including apartment or unit # |
| Time Zone | `timeZone` | options |  | The contact’s time zone. This can be set automatically by HubSpot based on other contact properties. It can also be set manually for each contact. |
| Twitter Username | `twitterUsername` | string |  | The contact's Twitter handle. This is set by HubSpot using the contact's email address. |
| Website URL | `websiteUrl` | string |  | The contact's company website |
| WhatsApp Phone Number | `whatsappPhoneNumber` | string |  | The phone number associated with the contact’s WhatsApp account |
| Work Email | `workEmail` | string |  | A contact's work email. This property is required for the Facebook Ads Integration. This property will be automatically synced via the Lead Ads tool |

</details>

| Options | `options` | collection | {} | ✗ | By default the response only includes the ID. If this option gets activated, it will resolve the data automatically. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Simplify Output | `resolveData` | boolean | False | By default the response only includes the ID. If this option gets activated, it will resolve the data automatically. |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact to Delete | `contactId` | resourceLocator |  | ✓ | This is not a contact's email but a number like 1485 | e.g. Select from the list |  |
| Company to Delete | `companyId` | resourceLocator |  | ✓ | e.g. Select from the list |  |
| Deal to Delete | `dealId` | resourceLocator |  | ✓ | e.g. Select from the list |  |
| Engagement to Delete | `engagementId` | resourceLocator |  | ✓ | e.g. Select from the list |  |
| Ticket to Delete | `ticketId` | resourceLocator |  | ✓ | e.g. Select from the list |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact to Get | `contactId` | resourceLocator |  | ✓ | This is not a contact's email but a number like 1485 | e.g. Select from the list |  |
| Options | `additionalFields` | collection | {} | ✗ | Specify which form submissions should be fetched | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Form Submission Mode | `formSubmissionMode` | options | all | Specify which form submissions should be fetched |
| Include List Memberships | `listMemberships` | boolean | True | Whether current list memberships should be fetched for the contact |
| Contact Properties to Include | `propertiesCollection` | fixedCollection | {} | Whether to include specific Contact properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Company to Get | `companyId` | resourceLocator |  | ✓ | e.g. Select from the list |  |
| Options | `additionalFields` | collection | {} | ✗ | Whether to return any merge history if the company has been previously merged with another company record. Defaults to false. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Merge Audits | `includeMergeAudits` | boolean | False | Whether to return any merge history if the company has been previously merged with another company record. Defaults to false. |

</details>

| Deal to Get | `dealId` | resourceLocator |  | ✓ | e.g. Select from the list |  |
| Filters | `filters` | collection | {} | ✗ | By default, you will only get data for the most recent version of a property in the "versions" data. If you include this parameter, you will get data for all previous versions. | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Property Versions | `includePropertyVersions` | boolean | False | By default, you will only get data for the most recent version of a property in the "versions" data. If you include this parameter, you will get data for all previous versions. |
| Deal Properties to Include | `propertiesCollection` | fixedCollection | {} | Whether to include specific Deal properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Engagement to Get | `engagementId` | resourceLocator |  | ✓ | e.g. Select from the list |  |
| Ticket to Get | `ticketId` | resourceLocator |  | ✓ | e.g. Select from the list |  |
| Options | `additionalFields` | collection | {} | ✗ | Whether to include specific Ticket properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Deleted | `includeDeleted` | boolean | False |  |
| Ticket Properties to Include | `properties` | multiOptions | [] | Whether to include specific Ticket properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Properties With History | `propertiesWithHistory` | string |  | Works similarly to properties=, but this parameter will include the history for the specified property, instead of just including the current value. Use this parameter when you need the full history of changes to a property's value. |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:250 |
| Options | `additionalFields` | collection | {} | ✗ | Specify which form submissions should be fetched | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Form Submission Mode | `formSubmissionMode` | options | all | Specify which form submissions should be fetched |
| Include List Memberships | `listMemberships` | boolean | True | Whether current list memberships should be fetched for the contact |
| Contact Properties to Include | `propertiesCollection` | fixedCollection | {} | Whether to include specific Contact properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:250 |
| Options | `options` | collection | {} | ✗ | Whether to return any merge history if a company has been previously merged with another company record. Defaults to false. | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Merge Audits | `includeMergeAudits` | boolean | False | Whether to return any merge history if a company has been previously merged with another company record. Defaults to false. |
| Company Properties to Include | `propertiesCollection` | fixedCollection | {} | Whether to include specific Company properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:250 |
| Options | `filters` | collection | {} | ✗ | Whether to include the IDs of the associated contacts and companies in the results. This will also automatically include the num_associated_contacts property. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Associations | `includeAssociations` | boolean | False | Whether to include the IDs of the associated contacts and companies in the results. This will also automatically include the num_associated_contacts property. |
| Deal Properties to Include | `properties` | multiOptions | [] | Include specific deal properties in the results. By default, the results will only include Deal ID and will not include the values for any properties for your Deals. |
| Deal Properties with History to Include | `propertiesWithHistory` | multiOptions | [] | Works similarly to properties, but this parameter will include the history for the specified property |
| Deal Properties to Include | `propertiesCollection` | fixedCollection | {} | Whether to include specific Deal properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:250 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:250 |
| Options | `additionalFields` | collection | {} | ✗ | Whether to include specific Ticket properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Ticket Properties to Include | `properties` | multiOptions | [] | Whether to include specific Ticket properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Properties With History | `propertiesWithHistory` | string |  | Works similarly to properties=, but this parameter will include the history for the specified property, instead of just including the current value. Use this parameter when you need the full history of changes to a property's value. |

</details>


### Get Recently Created/Updated parameters (`getRecentlyCreatedUpdated`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:250 |
| Options | `additionalFields` | collection | {} | ✗ | Specify which form submissions should be fetched | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Form Submission Mode | `formSubmissionMode` | options | all | Specify which form submissions should be fetched |
| Include List Memberships | `listMemberships` | boolean | True | Whether current list memberships should be fetched for the contact |
| Contact Properties to Include | `propertiesCollection` | fixedCollection | {} | Whether to include specific Contact properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:250 |
| Options | `additionalFields` | collection | {} | ✗ | Only return companys created after timestamp x. When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Since | `since` | dateTime |  | Only return companys created after timestamp x. When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format. |
| Company Properties to Include | `propertiesCollection` | fixedCollection | {} | Whether to include specific Company properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:250 |
| Options | `filters` | collection | {} | ✗ | Only return deals created after timestamp x. When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Since | `since` | dateTime |  | Only return deals created after timestamp x. When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format. |
| Include Property Versions | `includePropertyVersions` | boolean | False | By default, you will only get data for the most recent version of a property in the "versions" data. If you include this parameter, you will get data for all previous versions. |

</details>


### Search parameters (`search`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:250 |
| Filter Groups | `filterGroupsUi` | fixedCollection | {} | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Filter Group |  |

<details>
<summary><strong>Filter Groups sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filter Group | `filterGroupsValues` |  |  |  |

</details>

| Options | `additionalFields` | collection | {} | ✗ | Defines the direction in which search results are ordered. Default value is Descending. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Sort Order | `direction` | options | DESCENDING | Defines the direction in which search results are ordered. Default value is Descending. |
| Field Names or IDs | `properties` | multiOptions |  | Whether to include specific Contact properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Query | `query` | string |  | Perform a text search against all property values for an object type |
| Sort By | `sortBy` | options | createdate | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:250 |
| Filter Groups | `filterGroupsUi` | fixedCollection | {} | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Filter Group |  |

<details>
<summary><strong>Filter Groups sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Filter Group | `filterGroupsValues` |  |  |  |

</details>

| Options | `additionalFields` | collection | {} | ✗ | Defines the direction in which search results are ordered. Default value is Descending. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Direction | `direction` | options | DESCENDING | Defines the direction in which search results are ordered. Default value is Descending. |
| Field Names or IDs | `properties` | multiOptions | [] | Whether to include specific Deal properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Query | `query` | string |  | Perform a text search against all property values for an object type |
| Sort By | `sortBy` | options | createdate | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>


### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| By | `by` | options | email | ✓ |  |  |

**By options:**

* **Contact ID** (`id`)
* **Email** (`email`)

| Email | `email` | string |  | ✓ | e.g. name@email.com | email |
| Contact to Add | `id` | number |  | ✓ |  |  |
| List to Add To | `listId` | number |  | ✓ |  |  |

### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact to Remove | `id` | number |  | ✓ |  |  |
| List to Remove From | `listId` | number |  | ✓ |  |  |

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Name | `name` | string |  | ✓ |  |  |
| Company Properties | `additionalFields` | collection | {} | ✓ | The actual or estimated annual revenue of the company | e.g. Add Property |  |

<details>
<summary><strong>Company Properties sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| About Us | `aboutUs` | string |  |  |
| Annual Revenue | `annualRevenue` | number | 0 | The actual or estimated annual revenue of the company |
| City | `city` | string |  | The city where the company is located |
| Close Date | `closeDate` | dateTime |  | The date the company or organization was closed as a customer. When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format. |
| Company Domain Name | `companyDomainName` | string |  | The domain name of the company or organization |
| Company Owner Name or ID | `companyOwner` | options |  | The owner of the company. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Country/Region | `countryRegion` | string |  | The country/region in which the company or organization is located |
| Custom Properties | `customPropertiesUi` | fixedCollection | {} | Name of the property. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  | A short statement about the company's mission and goals |
| Facebook Fans | `facebookFans` | number | 0 | Number of facebook fans |
| Google Plus Page | `googlePlusPage` | string |  | The URL of the Google Plus page for the company or organization |
| Industry Name or ID | `industry` | options |  | The type of business the company performs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Is Public | `isPublic` | boolean | False | Whether that the company is publicly traded |
| Lead Status Name or ID | `leadStatus` | options |  | The company's sales, prospecting or outreach status. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Lifecycle Stage Name or ID | `lifecycleStatus` | options |  | The most advanced lifecycle stage across all contacts associated with this company or organization. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| LinkedIn Bio | `linkedinBio` | string |  | The LinkedIn bio for the company or organization |
| LinkedIn Company Page | `linkedInCompanyPage` | string |  | The URL of the LinkedIn company page for the company or organization |
| Number Of Employees | `numberOfEmployees` | number | 0 | The total number of employees who work for the company or organization |
| Original Source Type Name or ID | `originalSourceType` | options |  | Original source for the contact with the earliest activity for this company or organization. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Phone Number | `phoneNumber` | string |  | A company's primary phone number. Powered by HubSpot Insights. |
| Postal Code | `postalCode` | string |  | The postal or zip code of the company or organization. Powered by HubSpot Insights. |
| State/Region | `stateRegion` | string |  | The state or region in which the company or organization is located. Powered by HubSpot Insights. |
| Street Address | `streetAddress` | string |  | The street address of the company or organization, including unit number. Powered by HubSpot Insights. |
| Street Address 2 | `streetAddress2` | string |  | The additional address of the company or organization. Powered by HubSpot Insights. |
| Target Account Name or ID | `targetAccount` | options |  | The Target Account property is a means to flag high priority companies if you are following an account based strategy. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Timezone | `timezone` | string |  | The time zone where the company or organization is located. Powered by HubSpot Insights. |
| Total Money Raised | `totalMoneyRaised` | number | 0 | The total amount of money raised by the company. Powered by HubSpot Insights. |
| Twitter Bio | `twitterBio` | string |  | The Twitter bio of the company or organization |
| Twitter Followers | `twitterFollowers` | number | 0 | The number of Twitter followers of the company or organization |
| Twitter Handle | `twitterHandle` | string |  | The main twitter account of the company or organization |
| Type Name or ID | `type` | options |  | The optional classification of this company record - prospect, partner, etc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Web Technologies Name or ID | `webTechnologies` | options |  | The web technologies used by the company or organization. Powered by HubSpot Insights. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Website URL | `websiteUrl` | string |  | The main website of the company or organization. This property is used to identify unique companies. Powered by HubSpot Insights. |
| Year Founded | `yearFounded` | string |  | The year the company was created. Powered by HubSpot Insights. |

</details>

| Deal Stage Name or ID | `stage` | options |  | ✓ | The deal stage is required when creating a deal. See the CRM Pipelines API for details on managing pipelines and stages. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Deal Properties | `additionalFields` | collection | {} | ✓ | Whether to include specific Associated Company properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Deal Properties sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Amount | `amount` | string |  |  |
| Associated Company Names or IDs | `associatedCompany` | multiOptions | [] | Whether to include specific Associated Company properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Associated Vid Names or IDs | `associatedVids` | multiOptions | [] | Whether to include specific Associated Vid in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Close Date | `closeDate` | dateTime |  | When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format |
| Custom Properties | `customPropertiesUi` | fixedCollection | {} | Name of the property. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Deal Description | `description` | string |  |  |
| Deal Name | `dealName` | string |  |  |
| Deal Owner | `dealOwner` | resourceLocator |  | The HubSpot user to be assigned to the deal |
| Deal Type Name or ID | `dealType` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Pipeline Name or ID | `pipeline` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Type | `type` | options |  | ✓ |  |  |

**Type options:**

* **Call** (`call`)
* **Email** (`email`)
* **Meeting** (`meeting`)
* **Task** (`task`)

| Due Date | `dueDate` | dateTime |  | ✓ | The due date for the task |  |
| Metadata | `metadata` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Metadata sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Body | `body` | string |  |  |
| For Object Type | `forObjectType` | options |  |  |
| Status | `status` | options |  |  |
| Subject | `subject` | string |  |  |

</details>

| Metadata | `metadata` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Metadata sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| BCC | `bcc` | string |  |  |
| CC | `cc` | string |  |  |
| From Email | `fromEmail` | string |  |  |
| From First Name | `firstName` | string |  |  |
| From Last Name | `lastName` | string |  |  |
| HTML | `html` | string |  |  |
| Subject | `subject` | string |  |  |
| To Emails | `toEmail` | string |  |  |

</details>

| Metadata | `metadata` | collection | {} | ✗ | When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format | e.g. Add Field |  |

<details>
<summary><strong>Metadata sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Body | `body` | string |  |  |
| End Time | `endTime` | dateTime |  | When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format |
| Internal Meeting Notes | `internalMeetingNotes` | string |  |  |
| Start Time | `startTime` | dateTime |  | When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format |
| Title | `title` | string |  |  |

</details>

| Metadata | `metadata` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Metadata sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Body | `body` | string |  |  |
| Duration Milliseconds | `durationMilliseconds` | number | 0 |  |
| From Number | `fromNumber` | string |  |  |
| Recording URL | `recordingUrl` | string |  |  |
| Status | `status` | options | QUEUED |  |
| To Number | `toNumber` | string |  |  |

</details>

| Engagement Properties | `additionalFields` | collection | {} | ✗ | e.g. Add Property |  |

<details>
<summary><strong>Engagement Properties sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Associations | `associations` | collection | {} |  |

</details>

| Pipeline Name or ID | `pipelineId` | options |  | ✓ | The ID of the pipeline the ticket is in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Stage Name or ID | `stageId` | options |  | ✓ | The stage ID of the pipeline the ticket is in; depends on Pipeline ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Ticket Name | `ticketName` | string |  | ✓ |  |  |
| Ticket Properties | `additionalFields` | collection | {} | ✗ | Whether to include specific Company properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Property |  |

<details>
<summary><strong>Ticket Properties sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Company Names or IDs | `associatedCompanyIds` | multiOptions | [] | Whether to include specific Company properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Contact Names or IDs | `associatedContactIds` | multiOptions | [] | Whether to include specific Contact properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Category Name or ID | `category` | options |  | Main reason customer reached out for help. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Close Date | `closeDate` | dateTime |  | The date the ticket was closed. When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format. |
| Create Date | `createDate` | dateTime |  | The date the ticket was created. When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format. |
| Description | `description` | string |  | Description of the ticket |
| Priority Name or ID | `priority` | options |  | The level of attention needed on the ticket. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Resolution Name or ID | `resolution` | options |  | The action taken to resolve the ticket. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Source Name or ID | `source` | options |  | Channel where ticket was originally submitted. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Ticket Owner Name or ID | `ticketOwnerId` | options |  | The user from your team that the ticket is assigned to. You can assign additional users to a ticket record by creating a custom HubSpot user property. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Search parameters (`searchByDomain`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Domain | `domain` | string |  | ✓ | The company's website domain to search for, like n8n.io |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:250 |
| Options | `options` | collection | {} | ✗ | Whether to include specific Company properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Company Properties to Include | `properties` | multiOptions | [] | Whether to include specific Company properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Company to Update | `companyId` | resourceLocator |  | ✓ | e.g. Select from the list |  |
| Update Fields | `updateFields` | collection | {} | ✓ | The actual or estimated annual revenue of the company | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| About Us | `aboutUs` | string |  |  |
| Annual Revenue | `annualRevenue` | number | 0 | The actual or estimated annual revenue of the company |
| City | `city` | string |  | The city where the company is located |
| Close Date | `closeDate` | dateTime |  | The date the company or organization was closed as a customer. When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format. |
| Company Domain Name | `companyDomainName` | string |  | The domain name of the company or organization |
| Company Owner Name or ID | `companyOwner` | options |  | The owner of the company. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Country/Region | `countryRegion` | string |  | The country/region in which the company or organization is located |
| Custom Properties | `customPropertiesUi` | fixedCollection | {} | Name of the property. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Description | `description` | string |  | A short statement about the company's mission and goals |
| Facebook Fans | `facebookFans` | number | 0 | Number of facebook fans |
| Google Plus Page | `googlePlusPage` | string |  | The URL of the Google Plus page for the company or organization |
| Industry Name or ID | `industry` | options |  | The type of business the company performs. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Is Public | `isPublic` | boolean | False | Whether that the company is publicly traded |
| Lead Status Name or ID | `leadStatus` | options |  | The company's sales, prospecting or outreach status. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Lifecycle Stage Name or ID | `lifecycleStatus` | options |  | The most advanced lifecycle stage across all contacts associated with this company or organization. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Linkedin Bio | `linkedinBio` | string |  | The LinkedIn bio for the company or organization |
| LinkedIn Company Page | `linkedInCompanyPage` | string |  | The URL of the LinkedIn company page for the company or organization |
| Name | `name` | string |  |  |
| Number Of Employees | `numberOfEmployees` | number | 0 | The total number of employees who work for the company or organization |
| Original Source Type Name or ID | `originalSourceType` | options |  | Original source for the contact with the earliest activity for this company or organization. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Phone Number | `phoneNumber` | string |  | A company's primary phone number. Powered by HubSpot Insights. |
| Postal Code | `postalCode` | string |  | The postal or zip code of the company or organization. Powered by HubSpot Insights. |
| State/Region | `stateRegion` | string |  | The state or region in which the company or organization is located. Powered by HubSpot Insights. |
| Street Address | `streetAddress` | string |  | The street address of the company or organization, including unit number. Powered by HubSpot Insights. |
| Street Address 2 | `streetAddress2` | string |  | The additional address of the company or organization. Powered by HubSpot Insights. |
| Target Account Name or ID | `targetAccount` | options |  | The Target Account property is a means to flag high priority companies if you are following an account based strategy. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Timezone | `timezone` | string |  | The time zone where the company or organization is located. Powered by HubSpot Insights. |
| Total Money Raised | `totalMoneyRaised` | number | 0 | The total amount of money raised by the company. Powered by HubSpot Insights. |
| Twitter Bio | `twitterBio` | string |  | The Twitter bio of the company or organization |
| Twitter Followers | `twitterFollowers` | number | 0 | The number of Twitter followers of the company or organization |
| Twitter Handle | `twitterHandle` | string |  | The main twitter account of the company or organization |
| Type Name or ID | `type` | options |  | The optional classification of this company record - prospect, partner, etc. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Web Technologies Name or ID | `webTechnologies` | options |  | The web technologies used by the company or organization. Powered by HubSpot Insights. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Website URL | `websiteUrl` | string |  | The main website of the company or organization. This property is used to identify unique companies. Powered by HubSpot Insights. |
| Year Founded | `yearFounded` | string |  | The year the company was created. Powered by HubSpot Insights. |

</details>

| Deal to Update | `dealId` | resourceLocator |  | ✓ | e.g. Select from the list |  |
| Update Fields | `updateFields` | collection | {} | ✓ | When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format | e.g. Add Update Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Amount | `amount` | string |  |  |
| Close Date | `closeDate` | dateTime |  | When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format |
| Custom Properties | `customPropertiesUi` | fixedCollection | {} | Name of the property. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Deal Description | `description` | string |  |  |
| Deal Name | `dealName` | string |  |  |
| Deal Owner | `dealOwner` | resourceLocator |  | The HubSpot user to be assigned to the deal |
| Deal Stage Name or ID | `stage` | options |  | The deal stage is required when creating a deal. See the CRM Pipelines API for details on managing pipelines and stages. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Deal Type Name or ID | `dealType` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Pipeline | `pipeline` | string |  |  |

</details>

| Ticket to Update | `ticketId` | resourceLocator |  | ✓ | e.g. Select from the list |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Whether to include specific Company properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Company Names or IDs | `associatedCompanyIds` | multiOptions | [] | Whether to include specific Company properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Contact Names or IDs | `associatedContactIds` | multiOptions | [] | Whether to include specific Contact properties in the returned results. Choose from a list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Category Name or ID | `category` | options |  | Main reason customer reached out for help. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Close Date | `closeDate` | dateTime |  | The date the ticket was closed. When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format. |
| Create Date | `createDate` | dateTime |  | The date the ticket was created. When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format. |
| Description | `description` | string |  | Description of the ticket |
| Pipeline Name or ID | `pipelineId` | options |  | The ID of the pipeline the ticket is in. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Priority Name or ID | `priority` | options |  | The level of attention needed on the ticket. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Resolution Name or ID | `resolution` | options |  | The action taken to resolve the ticket. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Source Name or ID | `source` | options |  | Channel where ticket was originally submitted. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Stage Name or ID | `stageId` | options |  | The stage ID of the pipeline the ticket is in; depends on Pipeline ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Ticket Name | `ticketName` | string |  |  |
| Ticket Owner Name or ID | `ticketOwnerId` | options |  | The user from your team that the ticket is assigned to. You can assign additional users to a ticket record by creating a custom HubSpot user property. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


---

## Load Options Methods

- `getContactLeadStatuses`

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
node: HubSpot
displayName: HubSpot
description: Consume HubSpot API
version:
- '2'
- '2.1'
- '2.2'
nodeType: regular
group:
- output
credentials:
- name: hubspotApi
  required: true
- name: hubspotAppToken
  required: true
- name: hubspotOAuth2Api
  required: true
operations:
- id: upsert
  name: Create or Update
  description: Create a new contact, or update the current one if it already exists
    (upsert)
  params:
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: ''
    placeholder: name@email.com
    validation: &id017
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - contactList
          operation:
          - add
          by:
          - email
    typeInfo: &id018
      type: string
      displayName: Email
      name: email
- id: delete
  name: Delete
  description: Delete a contact
  params:
  - id: contactId
    name: Contact to Delete
    type: resourceLocator
    default: ''
    required: true
    description: This is not a contact's email but a number like 1485
    hint: To lookup a user by their email, use the Search operation
    placeholder: Select from the list
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - delete
    typeInfo: &id002
      type: resourceLocator
      displayName: Contact to Delete
      name: contactId
  - id: companyId
    name: Company to Delete
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Select from the list
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - company
          operation:
          - delete
    typeInfo: &id004
      type: resourceLocator
      displayName: Company to Delete
      name: companyId
  - id: dealId
    name: Deal to Delete
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Select from the list
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - delete
    typeInfo: &id006
      type: resourceLocator
      displayName: Deal to Delete
      name: dealId
  - id: engagementId
    name: Engagement to Delete
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Select from the list
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - engagement
          operation:
          - delete
    typeInfo: &id008
      type: resourceLocator
      displayName: Engagement to Delete
      name: engagementId
  - id: ticketId
    name: Ticket to Delete
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Select from the list
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - delete
    typeInfo: &id010
      type: resourceLocator
      displayName: Ticket to Delete
      name: ticketId
- id: get
  name: Get
  description: Get a contact
  params:
  - id: contactId
    name: Contact to Get
    type: resourceLocator
    default: ''
    required: true
    description: This is not a contact's email but a number like 1485
    hint: To lookup a user by their email, use the Search operation
    placeholder: Select from the list
    validation: *id001
    typeInfo: *id002
  - id: companyId
    name: Company to Get
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Select from the list
    validation: *id003
    typeInfo: *id004
  - id: dealId
    name: Deal to Get
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Select from the list
    validation: *id005
    typeInfo: *id006
  - id: engagementId
    name: Engagement to Get
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Select from the list
    validation: *id007
    typeInfo: *id008
  - id: ticketId
    name: Ticket to Get
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Select from the list
    validation: *id009
    typeInfo: *id010
- id: getAll
  name: Get Many
  description: Get many contacts
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id011
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - getAll
    typeInfo: &id012
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id013
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id014
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 250
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
    default: 100
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
    default: 100
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
    default: 100
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
    default: 100
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
- id: getRecentlyCreatedUpdated
  name: Get Recently Created/Updated
  description: Get recently created/updated contacts
  params:
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
    default: 100
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
    default: 100
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
    default: 100
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
- id: search
  name: Search
  description: Search contacts
  params:
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
    default: 100
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
  - id: filterGroupsUi
    name: Filter Groups
    type: fixedCollection
    default: {}
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Filter Group
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - search
    typeInfo: &id016
      type: fixedCollection
      displayName: Filter Groups
      name: filterGroupsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: filterGroupsValues
        displayName: Filter Group
        values:
        - displayName: Filters
          name: filtersUi
          type: fixedCollection
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          placeholder: Add Filter
          value: CONTAINS_TOKEN
          default: {}
          required: true
          options:
          - name: filterValues
            displayName: Filter
            values:
            - displayName: Property Name or ID
              name: propertyName
              type: options
              description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
              default: ''
              typeOptions:
                loadOptionsMethod: getDealProperties
            - displayName: Type
              name: type
              type: hidden
              default: ={{$parameter[
            - displayName: Operator
              name: operator
              type: options
              value: CONTAINS_TOKEN
              default: EQ
              options:
              - name: Contains Exactly
                value: CONTAINS_TOKEN
                displayName: Contains Exactly
              - name: Equal
                value: EQ
                displayName: Equal
              - name: Is Known
                value: HAS_PROPERTY
                displayName: Is Known
              - name: Is Unknown
                value: NOT_HAS_PROPERTY
                displayName: Is Unknown
              - name: Not Equal
                value: NEQ
                displayName: Not Equal
              displayOptions:
                hide:
                  type:
                  - number
            - displayName: Operator
              name: operator
              type: options
              value: CONTAINS_TOKEN
              default: EQ
              options:
              - name: Contains Exactly
                value: CONTAINS_TOKEN
                displayName: Contains Exactly
              - name: Equal
                value: EQ
                displayName: Equal
              - name: Greater Than
                value: GT
                displayName: Greater Than
              - name: Greater Than Or Equal
                value: GTE
                displayName: Greater Than Or Equal
              - name: Is Known
                value: HAS_PROPERTY
                displayName: Is Known
              - name: Is Unknown
                value: NOT_HAS_PROPERTY
                displayName: Is Unknown
              - name: Less Than
                value: LT
                displayName: Less Than
              - name: Less Than Or Equal
                value: LTE
                displayName: Less Than Or Equal
              - name: Not Equal
                value: NEQ
                displayName: Not Equal
              displayOptions:
                show:
                  type:
                  - number
            - displayName: Value
              name: value
              type: string
              default: ''
              required: true
              displayOptions:
                hide:
                  operator:
                  - HAS_PROPERTY
                  - NOT_HAS_PROPERTY
          typeOptions:
            multipleValues: true
          displayOptions:
            hide:
              type:
              - number
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
    default: 100
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
  - id: filterGroupsUi
    name: Filter Groups
    type: fixedCollection
    default: {}
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Filter Group
    validation: *id015
    typeInfo: *id016
- id: add
  name: Add
  description: Add contact to a list
  params:
  - id: by
    name: By
    type: options
    default: email
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - contactList
          operation:
          - add
    typeInfo:
      type: options
      displayName: By
      name: by
      possibleValues:
      - value: id
        name: Contact ID
        description: ''
      - value: email
        name: Email
        description: ''
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: ''
    placeholder: name@email.com
    validation: *id017
    typeInfo: *id018
  - id: id
    name: Contact to Add
    type: number
    default: ''
    required: true
    description: ''
    validation: &id019
      required: true
      displayOptions:
        show:
          resource:
          - contactList
          operation:
          - remove
    typeInfo: &id020
      type: number
      displayName: Contact to Remove
      name: id
  - id: listId
    name: List to Add To
    type: number
    default: ''
    required: true
    description: ''
    validation: &id021
      required: true
      displayOptions:
        show:
          resource:
          - contactList
          operation:
          - remove
    typeInfo: &id022
      type: number
      displayName: List to Remove From
      name: listId
- id: remove
  name: Remove
  description: Remove a contact from a list
  params:
  - id: id
    name: Contact to Remove
    type: number
    default: ''
    required: true
    description: ''
    validation: *id019
    typeInfo: *id020
  - id: listId
    name: List to Remove From
    type: number
    default: ''
    required: true
    description: ''
    validation: *id021
    typeInfo: *id022
- id: create
  name: Create
  description: Create a company
  params:
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - company
          operation:
          - create
    typeInfo:
      type: string
      displayName: Name
      name: name
  - id: stage
    name: Deal Stage Name or ID
    type: options
    default: ''
    required: true
    description: The deal stage is required when creating a deal. See the CRM Pipelines
      API for details on managing pipelines and stages. Choose from the list, or specify
      an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - create
    typeInfo:
      type: options
      displayName: Deal Stage Name or ID
      name: stage
      typeOptions:
        loadOptionsMethod: getDealStages
      possibleValues: []
  - id: type
    name: Type
    type: options
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - engagement
          operation:
          - create
    typeInfo:
      type: options
      displayName: Type
      name: type
      possibleValues:
      - value: call
        name: Call
        description: ''
      - value: email
        name: Email
        description: ''
      - value: meeting
        name: Meeting
        description: ''
      - value: task
        name: Task
        description: ''
  - id: dueDate
    name: Due Date
    type: dateTime
    default: ''
    required: true
    description: The due date for the task
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - engagement
          operation:
          - create
          type:
          - task
    typeInfo:
      type: dateTime
      displayName: Due Date
      name: dueDate
  - id: pipelineId
    name: Pipeline Name or ID
    type: options
    default: ''
    required: true
    description: The ID of the pipeline the ticket is in. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - create
    typeInfo:
      type: options
      displayName: Pipeline Name or ID
      name: pipelineId
      typeOptions:
        loadOptionsMethod: getTicketPipelines
      possibleValues: []
  - id: stageId
    name: Stage Name or ID
    type: options
    default: ''
    required: true
    description: The stage ID of the pipeline the ticket is in; depends on Pipeline
      ID. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - create
    typeInfo:
      type: options
      displayName: Stage Name or ID
      name: stageId
      typeOptions:
        loadOptionsMethod: getTicketStages
      possibleValues: []
  - id: ticketName
    name: Ticket Name
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - ticket
          operation:
          - create
    typeInfo:
      type: string
      displayName: Ticket Name
      name: ticketName
- id: searchByDomain
  name: Search
  description: Search companies by their website domain
  params:
  - id: domain
    name: Domain
    type: string
    default: ''
    required: true
    description: The company's website domain to search for, like n8n.io
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - company
          operation:
          - searchByDomain
    typeInfo:
      type: string
      displayName: Domain
      name: domain
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
    default: 100
    required: false
    description: Max number of results to return
    validation: *id013
    typeInfo: *id014
- id: update
  name: Update
  description: Update a company
  params:
  - id: companyId
    name: Company to Update
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Select from the list
    validation: *id003
    typeInfo: *id004
  - id: dealId
    name: Deal to Update
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Select from the list
    validation: *id005
    typeInfo: *id006
  - id: ticketId
    name: Ticket to Update
    type: resourceLocator
    default: ''
    required: true
    description: ''
    placeholder: Select from the list
    validation: *id009
    typeInfo: *id010
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods:
  - GET
  endpoints: []
  headers: []
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Property
  - field: options
    text: Add option
  - field: contactId
    text: Select from the list
  - field: additionalFields
    text: Add option
  - field: additionalFields
    text: Add option
  - field: contactId
    text: Select from the list
  - field: additionalFields
    text: Add option
  - field: filterGroupsUi
    text: Add Filter Group
  - field: additionalFields
    text: Add option
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Property
  - field: companyId
    text: Select from the list
  - field: updateFields
    text: Add Field
  - field: companyId
    text: Select from the list
  - field: additionalFields
    text: Add option
  - field: options
    text: Add Field
  - field: companyId
    text: Select from the list
  - field: additionalFields
    text: Add option
  - field: options
    text: Add option
  - field: additionalFields
    text: Add Field
  - field: dealId
    text: Select from the list
  - field: updateFields
    text: Add Update Field
  - field: dealId
    text: Select from the list
  - field: filters
    text: Add Filter
  - field: filters
    text: Add option
  - field: dealId
    text: Select from the list
  - field: filters
    text: Add option
  - field: filterGroupsUi
    text: Add Filter Group
  - field: additionalFields
    text: Add option
  - field: metadata
    text: Add Field
  - field: metadata
    text: Add Field
  - field: metadata
    text: Add Field
  - field: metadata
    text: Add Field
  - field: additionalFields
    text: Add Property
  - field: engagementId
    text: Select from the list
  - field: engagementId
    text: Select from the list
  - field: additionalFields
    text: Add Property
  - field: ticketId
    text: Select from the list
  - field: updateFields
    text: Add Field
  - field: ticketId
    text: Select from the list
  - field: additionalFields
    text: Add option
  - field: additionalFields
    text: Add option
  - field: ticketId
    text: Select from the list
  hints:
  - field: contactId
    text: To lookup a user by their email, use the Search operation
  - field: contactId
    text: To lookup a user by their email, use the Search operation
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
  "$id": "https://n8n.io/schemas/nodes/HubSpot.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "HubSpot Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "upsert",
        "delete",
        "get",
        "getAll",
        "getRecentlyCreatedUpdated",
        "search",
        "add",
        "remove",
        "create",
        "searchByDomain",
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
            "apiKey",
            "appToken",
            "oAuth2"
          ],
          "default": "apiKey"
        },
        "resource": {
          "description": "",
          "type": "string",
          "enum": [
            "company",
            "contact",
            "contactList",
            "deal",
            "engagement",
            "form",
            "ticket"
          ],
          "default": "contact"
        },
        "operation": {
          "description": "Create a ticket",
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
        "email": {
          "description": "",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "additionalFields": {
          "description": "Whether to include specific Ticket properties in the returned results. Choose from a list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "options": {
          "description": "Whether to include specific Company properties in the returned results. Choose from a list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "contactId": {
          "description": "This is not a contact's email but a number like 1485",
          "type": "string",
          "examples": [
            "Select from the list"
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
        "filterGroupsUi": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter Group"
          ]
        },
        "by": {
          "description": "",
          "type": "string",
          "enum": [
            "id",
            "email"
          ],
          "default": "email"
        },
        "id": {
          "description": "",
          "type": "number",
          "default": ""
        },
        "listId": {
          "description": "",
          "type": "number",
          "default": ""
        },
        "name": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "companyId": {
          "description": "",
          "type": "string",
          "examples": [
            "Select from the list"
          ]
        },
        "updateFields": {
          "description": "Whether to include specific Company properties in the returned results. Choose from a list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>. Choose from the list, or specify IDs using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "domain": {
          "description": "The company's website domain to search for, like n8n.io",
          "type": "string",
          "default": ""
        },
        "stage": {
          "description": "The deal stage is required when creating a deal. See the CRM Pipelines API for details on managing pipelines and stages. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "dealId": {
          "description": "",
          "type": "string",
          "examples": [
            "Select from the list"
          ]
        },
        "filters": {
          "description": "Only return deals created after timestamp x. When using expressions, the time should be specified in YYYY-MM-DD hh-mm-ss format.",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "type": {
          "description": "",
          "type": "string",
          "enum": [
            "call",
            "email",
            "meeting",
            "task"
          ],
          "default": ""
        },
        "dueDate": {
          "description": "The due date for the task",
          "type": "string",
          "default": ""
        },
        "metadata": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "engagementId": {
          "description": "",
          "type": "string",
          "examples": [
            "Select from the list"
          ]
        },
        "pipelineId": {
          "description": "The ID of the pipeline the ticket is in. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "stageId": {
          "description": "The stage ID of the pipeline the ticket is in; depends on Pipeline ID. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "ticketName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "ticketId": {
          "description": "",
          "type": "string",
          "examples": [
            "Select from the list"
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
    "version": [
      "2",
      "2.1",
      "2.2"
    ]
  },
  "credentials": [
    {
      "name": "hubspotApi",
      "required": true
    },
    {
      "name": "hubspotAppToken",
      "required": true
    },
    {
      "name": "hubspotOAuth2Api",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['2', '2.1', '2.2'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
