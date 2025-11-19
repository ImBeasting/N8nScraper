---
title: "Node: Keap"
slug: "node-keap"
version: "1"
updated: "2025-11-13"
summary: "Consume Keap API"
node_type: "regular"
group: "['input']"
---

# Node: Keap

**Purpose.** Consume Keap API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:keap.png`
- **Group:** `['input']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **keapOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `keapOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Company Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a company |
| Get Many | `getAll` | Retrieve many companies |

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create or Update | `upsert` | Create a new contact, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete an contact |
| Get | `get` | Retrieve an contact |
| Get Many | `getAll` | Retrieve many contacts |

### Contactnote Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a note |
| Delete | `delete` | Delete a note |
| Get | `get` | Get a notes |
| Get Many | `getAll` | Retrieve many notes |
| Update | `update` | Update a note |

### Contacttag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Add a list of tags to a contact |
| Delete | `delete` | Delete a contact's tag |
| Get Many | `getAll` | Retrieve many contact's tags |

### Ecommerceorder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an ecommerce order |
| Get | `get` | Get an ecommerce order |
| Delete | `delete` | Delete an ecommerce order |
| Get Many | `getAll` | Retrieve many ecommerce orders |

### Ecommerceproduct Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an ecommerce product |
| Delete | `delete` | Delete an ecommerce product |
| Get | `get` | Get an ecommerce product |
| Get Many | `getAll` | Retrieve many ecommerce products |

### Email Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create Record | `createRecord` | Create a record of an email sent to a contact |
| Get Many | `getAll` | Retrieve many sent emails |
| Send | `send` | Send Email |

### File Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Delete | `delete` | Delete a file |
| Get Many | `getAll` | Retrieve many files |
| Upload | `upload` | Upload a file |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | company | ✗ | Resource to operate on |  |

**Resource options:**

* **Company** (`company`)
* **Contact** (`contact`)
* **Contact Note** (`contactNote`)
* **Contact Tag** (`contactTag`)
* **Ecommerce Order** (`ecommerceOrder`)
* **Ecommerce Product** (`ecommerceProduct`)
* **Email** (`email`)
* **File** (`file`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a company |  |

**Operation options:**

* **Create** (`create`) - Create a company
* **Get Many** (`getAll`) - Retrieve many companies

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Company Name | `companyName` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `emailAddress` | string |  |  |
| Notes | `notes` | string |  |  |
| Opt In Reason | `optInReason` | string |  |  |
| Website | `website` | string |  |  |

</details>

| Addresses | `addressesUi` | fixedCollection | {} | ✗ | ISO Alpha-3 Code | e.g. Add Address |  |

<details>
<summary><strong>Addresses sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `addressesValues` |  |  |  |

</details>

| Faxes | `faxesUi` | fixedCollection | {} | ✗ | e.g. Add Fax |  |

<details>
<summary><strong>Faxes sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fax | `faxesValues` |  |  |  |

</details>

| Phones | `phonesUi` | fixedCollection | {} | ✗ | e.g. Add Phone |  |

<details>
<summary><strong>Phones sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Phones | `phonesValues` |  |  |  |

</details>

| User Name or ID | `userId` | options |  | ✗ | The infusionsoft user to create the note on behalf of. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Contact ID | `contactId` | string |  | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Body | `body` | string |  |  |
| Title | `title` | string |  |  |
| Type | `type` | options |  |  |

</details>

| Contact ID | `contactId` | string |  | ✓ |  |  |
| Tag Names or IDs | `tagIds` | multiOptions | [] | ✓ | Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Contact ID | `contactId` | string |  | ✓ |  |  |
| Order Date | `orderDate` | dateTime |  | ✓ |  |  |
| Order Title | `orderTitle` | string |  | ✓ |  |  |
| Order Type | `orderType` | options |  | ✓ |  |  |

**Order Type options:**

* **Offline** (`offline`)
* **Online** (`online`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Uses multiple strings separated by comma as promo codes. The corresponding discount will be applied to the order. | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Lead Affiliate ID | `leadAffiliateId` | number | 0 |  |
| Promo Codes | `promoCodes` | string |  | Uses multiple strings separated by comma as promo codes. The corresponding discount will be applied to the order. |
| Sales Affiliate ID | `salesAffiliateId` | number | 0 |  |

</details>

| Shipping Address | `addressUi` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Address |  |

<details>
<summary><strong>Shipping Address sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `addressValues` |  |  |  |

</details>

| Order Items | `orderItemsUi` | fixedCollection | {} | ✗ | Overridable price of the product, if not specified, the default will be used | e.g. Add Order Item |  |

<details>
<summary><strong>Order Items sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Order Item | `orderItemsValues` |  |  |  |

</details>

| Product Name | `productName` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Active | `active` | boolean | False |  |
| Product Description | `productDesc` | string |  |  |
| Product Price | `productPrice` | number | 0 |  |
| Product Short Desc | `productShortDesc` | string |  |  |
| SKU | `sku` | string |  |  |
| Subscription Only | `subscriptionOnly` | boolean | False |  |

</details>


### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:200 |
| Options | `options` | collection | {} | ✗ | Company name to query on | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Company Name | `companyName` | string |  | Company name to query on |
| Order | `order` | options |  | Attribute to order items by |
| Order Direction | `orderDirection` | options |  |  |
| Fields | `fields` | string |  | Comma-delimited list of Company properties to include in the response. (Fields such as notes, fax_number and custom_fields aren't included, by default.). |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:200 |
| Options | `options` | collection | {} | ✗ | Attribute to order items by | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `email` | string |  |  |
| Given Name | `givenName` | string |  |  |
| Family Name | `familyName` | string |  |  |
| Order | `order` | options |  | Attribute to order items by |
| Order Direction | `orderDirection` | options |  |  |
| Since | `since` | dateTime |  | Date to start searching from on LastUpdated |
| Until | `until` | dateTime |  | Date to search to on LastUpdated |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:200 |
| Filters | `filters` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Filter | min:0, max:∞ |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Contact ID | `contactId` | number | 0 |  |
| User Name or ID | `userId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Contact ID | `contactId` | string |  | ✓ |  |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:200 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:200 |
| Options | `options` | collection | {} | ✗ | Date to start searching from | e.g. Add option | min:0, max:∞ |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Since | `since` | dateTime |  | Date to start searching from |
| Until | `until` | dateTime |  | Date to search to |
| Paid | `paid` | boolean | False |  |
| Order | `order` | string |  | Attribute to order items by |
| Contact ID | `contactId` | number | 0 |  |
| Product ID | `productId` | number | 0 |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:200 |
| Filters | `filters` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Active | `active` | boolean | False |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:200 |
| Filters | `filters` | collection | {} | ✗ | Emails sent since the provided date, must be present if untilDate is provided | e.g. Add Filter | min:0, max:∞ |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Contact ID | `contactId` | number | 0 |  |
| Email | `email` | string |  |  |
| Since Sent Date | `sinceSentDate` | dateTime |  | Emails sent since the provided date, must be present if untilDate is provided |
| Until Sent Date | `untilSentDate` | dateTime |  | Email sent until the provided date |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:200 |
| Filters | `filters` | collection | {} | ✗ | Filter based on Contact ID, if user has permission to see Contact files | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Contact ID | `contactId` | number | 0 | Filter based on Contact ID, if user has permission to see Contact files |
| Name | `name` | string |  | Filter files based on name, with '*' preceding or following to indicate LIKE queries |
| Permission | `permission` | options | both | Filter based on the permission of files |
| Type | `type` | options |  | Filter based on the type of file |
| Viewable | `viewable` | options | both | Include public or private files in response |

</details>


### Create or Update parameters (`upsert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Duplicate Option | `duplicateOption` | options | email | ✓ | Performs duplicate checking by one of the following options: Email, EmailAndName. If a match is found using the option provided, the existing contact will be updated. |  |

**Duplicate Option options:**

* **Email** (`email`)
* **Email And Name** (`emailAndName`)

| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Anniversary | `anniversary` | dateTime |  |  |
| Company ID | `companyId` | number | 0 |  |
| Contact Type Name or ID | `contactType` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Family Name | `familyName` | string |  |  |
| Given Name | `givenName` | string |  |  |
| IP Address | `ipAddress` | string |  |  |
| Job Title | `jobTitle` | string |  |  |
| Lead Source ID | `leadSourceId` | number | 0 |  |
| Middle Name | `middleName` | string |  |  |
| Opt In Reason | `optInReason` | string |  |  |
| Owner Name or ID | `ownerId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Preferred Locale | `preferredLocale` | string |  |  |
| Preferred Name | `preferredName` | string |  |  |
| Source Type | `sourceType` | options |  |  |
| Spouse Name | `spouseName` | string |  |  |
| Timezone Name or ID | `timezone` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Website | `website` | string |  |  |

</details>

| Addresses | `addressesUi` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Address |  |

<details>
<summary><strong>Addresses sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address | `addressesValues` |  |  |  |

</details>

| Emails | `emailsUi` | fixedCollection | {} | ✗ | e.g. Add Email | email |

<details>
<summary><strong>Emails sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Email | `emailsValues` |  |  |  |

</details>

| Faxes | `faxesUi` | fixedCollection | {} | ✗ | e.g. Add Fax |  |

<details>
<summary><strong>Faxes sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fax | `faxesValues` |  |  |  |

</details>

| Phones | `phonesUi` | fixedCollection | {} | ✗ | e.g. Add Phone |  |

<details>
<summary><strong>Phones sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Phones | `phonesValues` |  |  |  |

</details>

| Social Accounts | `socialAccountsUi` | fixedCollection | {} | ✗ | e.g. Add Social Account |  |

<details>
<summary><strong>Social Accounts sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Social Account | `socialAccountsValues` |  |  |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ |  |  |
| Note ID | `noteId` | string |  | ✓ |  |  |
| Contact ID | `contactId` | string |  | ✓ |  |  |
| Tag IDs | `tagIds` | string | Tag IDs, multiple IDs can be set separated by comma. | ✓ |  |  |
| Order ID | `orderId` | string |  | ✓ |  |  |
| Product ID | `productId` | string |  | ✓ |  |  |
| File ID | `fileId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact ID | `contactId` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | Comma-delimited list of Contact properties to include in the response. (Some fields such as lead_source_id, custom_fields, and job_title aren't included, by default.). | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Fields | `fields` | string |  | Comma-delimited list of Contact properties to include in the response. (Some fields such as lead_source_id, custom_fields, and job_title aren't included, by default.). |

</details>

| Note ID | `noteId` | string |  | ✓ |  |  |
| Order ID | `orderId` | string |  | ✓ |  |  |
| Product ID | `productId` | string |  | ✓ |  |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Note ID | `noteId` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The infusionsoft user to create the note on behalf of. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Body | `body` | string |  |  |
| Contact ID | `contactId` | number | 0 |  |
| Title | `title` | string |  |  |
| Type | `type` | options |  |  |
| User Name or ID | `userId` | options |  | The infusionsoft user to create the note on behalf of. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Create Record parameters (`createRecord`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Sent To Address | `sentToAddress` | string |  | ✓ |  |  |
| Sent From Address | `sentFromAddress` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Base64 encoded HTML | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Clicked Date | `clickedDate` | dateTime |  |  |
| Contact ID | `contactId` | number | 0 |  |
| Headers | `headers` | string |  |  |
| HTML Content | `htmlContent` | string |  | Base64 encoded HTML |
| Opened Date | `openedDate` | dateTime |  |  |
| Original Provider | `originalProvider` | options | UNKNOWN | Provider that sent the email case insensitive, must be in list |
| Original Provider ID | `originalProviderId` | string |  | Provider ID that sent the email, must be unique when combined with provider. If omitted a UUID without dashes is autogenerated for the record. |
| Plain Content | `plainContent` | string |  | Base64 encoded text |
| Provider Source ID | `providerSourceId` | string | The email address of the synced email account that generated this message. |  |
| Received Date | `receivedDate` | dateTime |  |  |
| Sent Date | `sentDate` | dateTime |  |  |
| Sent From Reply Address | `sentFromReplyAddress` | string |  |  |
| Sent To Bcc Addresses | `sentToBccAddresses` | string |  |  |
| Sent To CC Addresses | `sentToCCAddresses` | string |  |  |
| Subject | `subject` | string |  |  |

</details>


### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| User Name or ID | `userId` | options |  | ✓ | The infusionsoft user to send the email on behalf of. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Contact IDs | `contactIds` | string |  | ✗ | Contact IDs to receive the email. Multiple can be added seperated by comma. |  |
| Subject | `subject` | string |  | ✗ | The subject line of the email |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Email field of each Contact record to address the email to, such as 'EmailAddress1', 'EmailAddress2', 'EmailAddress3', defaulting to the contact's primary email | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Address Field | `addressField` | string |  | Email field of each Contact record to address the email to, such as 'EmailAddress1', 'EmailAddress2', 'EmailAddress3', defaulting to the contact's primary email |
| HTML Content | `htmlContent` | string |  | The HTML-formatted content of the email, encoded in Base64 |
| Plain Content | `plainContent` | string |  | The plain-text content of the email, encoded in Base64 |

</details>

| Attachments | `attachmentsUi` | fixedCollection |  | ✗ | The content of the attachment, encoded in Base64 | e.g. Add Attachments |  |

<details>
<summary><strong>Attachments sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Attachments Values | `attachmentsValues` |  |  |  |
| Attachments Binary | `attachmentsBinary` |  |  |  |

</details>


### Upload parameters (`upload`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Binary File | `binaryData` | boolean | False | ✗ | Whether the data to upload should be taken from binary field |  |
| Input Binary Field | `binaryPropertyName` | string | data | ✓ | e.g. The name of the input binary field containing the file to be uploaded |  |
| File Association | `fileAssociation` | options |  | ✓ |  |  |

**File Association options:**

* **Company** (`company`)
* **Contact** (`contact`)
* **User** (`user`)

| Contact ID | `contactId` | string |  | ✓ |  |  |
| File Name | `fileName` | string |  | ✓ | The filename of the attached file, including extension |  |
| File Data | `fileData` | string |  | ✓ | The content of the attachment, encoded in Base64 |  |
| Is Public | `isPublic` | boolean | False | ✗ |  |  |

---

## Load Options Methods

- `getTags`
- `for`
- `name`
- `value`

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
* Aliases: Infusionsoft

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: keap
displayName: Keap
description: Consume Keap API
version: '1'
nodeType: regular
group:
- input
credentials:
- name: keapOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a company
  params:
  - id: companyName
    name: Company Name
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - company
    typeInfo:
      type: string
      displayName: Company Name
      name: companyName
  - id: addressesUi
    name: Addresses
    type: fixedCollection
    default: {}
    required: false
    description: ISO Alpha-3 Code
    placeholder: Add Address
    validation: &id007
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - upsert
    typeInfo: &id008
      type: fixedCollection
      displayName: Addresses
      name: addressesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: addressesValues
        displayName: Address
        values:
        - displayName: Field
          name: field
          type: options
          value: BILLING
          default: ''
          options:
          - name: Billing
            value: BILLING
            displayName: Billing
          - name: Shipping
            value: SHIPPING
            displayName: Shipping
          - name: Other
            value: OTHER
            displayName: Other
        - displayName: Country Code Name or ID
          name: countryCode
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getCountries
        - displayName: Line 1
          name: line1
          type: string
          default: ''
        - displayName: Line 2
          name: line2
          type: string
          default: ''
        - displayName: Locality
          name: locality
          type: string
          default: ''
        - displayName: Postal Code
          name: postalCode
          type: string
          default: ''
        - displayName: Region
          name: region
          type: string
          default: ''
        - displayName: Zip Code
          name: zipCode
          type: string
          default: ''
        - displayName: Zip Four
          name: zipFour
          type: string
          default: ''
  - id: faxesUi
    name: Faxes
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Fax
    validation: &id009
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - upsert
    typeInfo: &id010
      type: fixedCollection
      displayName: Faxes
      name: faxesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: faxesValues
        displayName: Fax
        values:
        - displayName: Field
          name: field
          type: options
          value: FAX1
          default: ''
          options:
          - name: Fax 1
            value: FAX1
            displayName: Fax 1
          - name: Fax 2
            value: FAX2
            displayName: Fax 2
        - displayName: Number
          name: number
          type: string
          default: ''
  - id: phonesUi
    name: Phones
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Phone
    validation: &id011
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - upsert
    typeInfo: &id012
      type: fixedCollection
      displayName: Phones
      name: phonesUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: phonesValues
        displayName: Phones
        values:
        - displayName: Field
          name: field
          type: options
          value: PHONE1
          default: ''
          options:
          - name: Phone 1
            value: PHONE1
            displayName: Phone 1
          - name: Phone 2
            value: PHONE2
            displayName: Phone 2
          - name: Phone 3
            value: PHONE3
            displayName: Phone 3
          - name: Phone 4
            value: PHONE4
            displayName: Phone 4
          - name: Phone 5
            value: PHONE5
            displayName: Phone 5
        - displayName: Number
          name: number
          type: string
          default: ''
  - id: userId
    name: User Name or ID
    type: options
    default: ''
    required: false
    description: The infusionsoft user to create the note on behalf of. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id021
      required: true
      displayOptions:
        show:
          operation:
          - send
          resource:
          - email
    typeInfo: &id022
      type: options
      displayName: User Name or ID
      name: userId
      typeOptions:
        loadOptionsMethod: getUsers
      possibleValues: []
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: false
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
          fileAssociation:
          - contact
    typeInfo: &id002
      type: string
      displayName: Contact ID
      name: contactId
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: tagIds
    name: Tag Names or IDs
    type: multiOptions
    default: []
    required: true
    description: Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id013
      required: true
      displayOptions:
        show:
          operation:
          - delete
          resource:
          - contactTag
    typeInfo: &id014
      type: string
      displayName: Tag IDs
      name: tagIds
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: orderDate
    name: Order Date
    type: dateTime
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - ecommerceOrder
    typeInfo:
      type: dateTime
      displayName: Order Date
      name: orderDate
  - id: orderTitle
    name: Order Title
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - ecommerceOrder
    typeInfo:
      type: string
      displayName: Order Title
      name: orderTitle
  - id: orderType
    name: Order Type
    type: options
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - ecommerceOrder
    typeInfo:
      type: options
      displayName: Order Type
      name: orderType
      possibleValues:
      - value: offline
        name: Offline
        description: ''
      - value: online
        name: Online
        description: ''
  - id: addressUi
    name: Shipping Address
    type: fixedCollection
    default: {}
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Address
    validation:
      displayOptions:
        show:
          resource:
          - ecommerceOrder
          operation:
          - create
    typeInfo:
      type: fixedCollection
      displayName: Shipping Address
      name: addressUi
      typeOptions:
        multipleValues: false
      subProperties:
      - name: addressValues
        displayName: Address
        values:
        - displayName: Company
          name: company
          type: string
          default: ''
        - displayName: Country Code Name or ID
          name: countryCode
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getCountries
        - displayName: First Name
          name: firstName
          type: string
          default: ''
        - displayName: Middle Name
          name: middleName
          type: string
          default: ''
        - displayName: Last Name
          name: lastName
          type: string
          default: ''
        - displayName: Line 1
          name: line1
          type: string
          default: ''
        - displayName: Line 2
          name: line2
          type: string
          default: ''
        - displayName: Locality
          name: locality
          type: string
          default: ''
        - displayName: Region
          name: region
          type: string
          default: ''
        - displayName: Zip Code
          name: zipCode
          type: string
          default: ''
        - displayName: Zip Four
          name: zipFour
          type: string
          default: ''
        - displayName: Phone
          name: phone
          type: string
          default: ''
  - id: orderItemsUi
    name: Order Items
    type: fixedCollection
    default: {}
    required: false
    description: Overridable price of the product, if not specified, the default will
      be used
    placeholder: Add Order Item
    validation:
      displayOptions:
        show:
          resource:
          - ecommerceOrder
          operation:
          - create
    typeInfo:
      type: fixedCollection
      displayName: Order Items
      name: orderItemsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: orderItemsValues
        displayName: Order Item
        values:
        - displayName: Description
          name: description
          type: string
          default: ''
        - displayName: Price
          name: price
          type: number
          description: Overridable price of the product, if not specified, the default
            will be used
          default: 0
          typeOptions:
            minValue: 0
        - displayName: Product ID
          name: product ID
          type: number
          default: 0
          typeOptions:
            minValue: 0
        - displayName: Quantity
          name: quantity
          type: number
          default: 1
          typeOptions:
            minValue: 1
  - id: productName
    name: Product Name
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - ecommerceProduct
    typeInfo:
      type: string
      displayName: Product Name
      name: productName
- id: getAll
  name: Get Many
  description: Retrieve many companies
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
          - file
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
          - file
          returnAll:
          - false
    typeInfo: &id006
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 200
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
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
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
- id: upsert
  name: Create or Update
  description: Create a new contact, or update the current one if it already exists
    (upsert)
  params:
  - id: duplicateOption
    name: Duplicate Option
    type: options
    default: email
    required: true
    description: 'Performs duplicate checking by one of the following options: Email,
      EmailAndName. If a match is found using the option provided, the existing contact
      will be updated.'
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - upsert
          resource:
          - contact
    typeInfo:
      type: options
      displayName: Duplicate Option
      name: duplicateOption
      possibleValues:
      - value: email
        name: Email
        description: ''
      - value: emailAndName
        name: Email And Name
        description: ''
  - id: addressesUi
    name: Addresses
    type: fixedCollection
    default: {}
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Address
    validation: *id007
    typeInfo: *id008
  - id: emailsUi
    name: Emails
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Email
    validation:
      format: email
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - upsert
    typeInfo:
      type: fixedCollection
      displayName: Emails
      name: emailsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: emailsValues
        displayName: Email
        values:
        - displayName: Field
          name: field
          type: options
          value: EMAIL1
          default: ''
          options:
          - name: Email 1
            value: EMAIL1
            displayName: Email 1
          - name: Email 2
            value: EMAIL2
            displayName: Email 2
          - name: Email 3
            value: EMAIL3
            displayName: Email 3
        - displayName: Email
          name: email
          type: string
          placeholder: name@email.com
          default: ''
  - id: faxesUi
    name: Faxes
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Fax
    validation: *id009
    typeInfo: *id010
  - id: phonesUi
    name: Phones
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Phone
    validation: *id011
    typeInfo: *id012
  - id: socialAccountsUi
    name: Social Accounts
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Social Account
    validation:
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - upsert
    typeInfo:
      type: fixedCollection
      displayName: Social Accounts
      name: socialAccountsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: socialAccountsValues
        displayName: Social Account
        values:
        - displayName: Type
          name: type
          type: options
          value: Facebook
          default: ''
          options:
          - name: Facebook
            value: Facebook
            displayName: Facebook
          - name: Twitter
            value: Twitter
            displayName: Twitter
          - name: LinkedIn
            value: LinkedIn
            displayName: Linked In
        - displayName: Name
          name: name
          type: string
          default: ''
- id: delete
  name: Delete
  description: Delete an contact
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: noteId
    name: Note ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id015
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - contactNote
    typeInfo: &id016
      type: string
      displayName: Note ID
      name: noteId
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: tagIds
    name: Tag IDs
    type: string
    default: Tag IDs, multiple IDs can be set separated by comma.
    required: true
    description: ''
    validation: *id013
    typeInfo: *id014
  - id: orderId
    name: Order ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id017
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - ecommerceOrder
    typeInfo: &id018
      type: string
      displayName: Order ID
      name: orderId
  - id: productId
    name: Product ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id019
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - ecommerceProduct
    typeInfo: &id020
      type: string
      displayName: Product ID
      name: productId
  - id: fileId
    name: File ID
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - delete
          resource:
          - file
    typeInfo:
      type: string
      displayName: File ID
      name: fileId
- id: get
  name: Get
  description: Retrieve an contact
  params:
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: noteId
    name: Note ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id015
    typeInfo: *id016
  - id: orderId
    name: Order ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id017
    typeInfo: *id018
  - id: productId
    name: Product ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id019
    typeInfo: *id020
- id: update
  name: Update
  description: Update a note
  params:
  - id: noteId
    name: Note ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id015
    typeInfo: *id016
- id: createRecord
  name: Create Record
  description: Create a record of an email sent to a contact
  params:
  - id: sentToAddress
    name: Sent To Address
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - createRecord
          resource:
          - email
    typeInfo:
      type: string
      displayName: Sent To Address
      name: sentToAddress
  - id: sentFromAddress
    name: Sent From Address
    type: string
    default: ''
    required: true
    description: ''
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - createRecord
          resource:
          - email
    typeInfo:
      type: string
      displayName: Sent From Address
      name: sentFromAddress
- id: send
  name: Send
  description: Send Email
  params:
  - id: userId
    name: User Name or ID
    type: options
    default: ''
    required: true
    description: The infusionsoft user to send the email on behalf of. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id021
    typeInfo: *id022
  - id: contactIds
    name: Contact IDs
    type: string
    default: ''
    required: false
    description: Contact IDs to receive the email. Multiple can be added seperated
      by comma.
    validation:
      displayOptions:
        show:
          operation:
          - send
          resource:
          - email
    typeInfo:
      type: string
      displayName: Contact IDs
      name: contactIds
  - id: subject
    name: Subject
    type: string
    default: ''
    required: false
    description: The subject line of the email
    validation:
      displayOptions:
        show:
          operation:
          - send
          resource:
          - email
    typeInfo:
      type: string
      displayName: Subject
      name: subject
  - id: attachmentsUi
    name: Attachments
    type: fixedCollection
    default: ''
    required: false
    description: The content of the attachment, encoded in Base64
    placeholder: Add Attachments
    validation:
      displayOptions:
        show:
          operation:
          - send
          resource:
          - email
    typeInfo:
      type: fixedCollection
      displayName: Attachments
      name: attachmentsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: attachmentsValues
        displayName: Attachments Values
        values:
        - displayName: File Data
          name: fileData
          type: string
          description: The content of the attachment, encoded in Base64
          default: ''
        - displayName: File Name
          name: fileName
          type: string
          description: The filename of the attached file, including extension
          default: ''
      - name: attachmentsBinary
        displayName: Attachments Binary
        values:
        - displayName: Property
          name: property
          type: string
          description: Name of the binary properties which contain data which should
            be added to email as attachment
          default: ''
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
  - id: binaryPropertyName
    name: Input Binary Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the input binary field containing the file to be uploaded
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
          binaryData:
          - true
    typeInfo:
      type: string
      displayName: Input Binary Field
      name: binaryPropertyName
  - id: fileAssociation
    name: File Association
    type: options
    default: ''
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
      type: options
      displayName: File Association
      name: fileAssociation
      possibleValues:
      - value: company
        name: Company
        description: ''
      - value: contact
        name: Contact
        description: ''
      - value: user
        name: User
        description: ''
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: fileName
    name: File Name
    type: string
    default: ''
    required: true
    description: The filename of the attached file, including extension
    validation:
      required: true
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
      displayName: File Name
      name: fileName
  - id: fileData
    name: File Data
    type: string
    default: ''
    required: true
    description: The content of the attachment, encoded in Base64
    validation:
      required: true
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
      displayName: File Data
      name: fileData
  - id: isPublic
    name: Is Public
    type: boolean
    default: false
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - upload
          resource:
          - file
    typeInfo:
      type: boolean
      displayName: Is Public
      name: isPublic
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
  - field: addressesUi
    text: Add Address
  - field: faxesUi
    text: Add Fax
  - field: phonesUi
    text: Add Phone
  - field: options
    text: Add option
  - field: additionalFields
    text: Add Field
  - field: addressesUi
    text: Add Address
  - field: emailsUi
    text: Add Email
  - field: faxesUi
    text: Add Fax
  - field: phonesUi
    text: Add Phone
  - field: socialAccountsUi
    text: Add Social Account
  - field: options
    text: Add option
  - field: options
    text: Add option
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: addressUi
    text: Add Address
  - field: orderItemsUi
    text: Add Order Item
  - field: options
    text: Add option
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: additionalFields
    text: Add Field
  - field: attachmentsUi
    text: Add Attachments
  - field: filters
    text: Add Field
  hints:
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
  "$id": "https://n8n.io/schemas/nodes/keap.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Keap Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "getAll",
        "upsert",
        "delete",
        "get",
        "update",
        "createRecord",
        "send",
        "upload"
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
            "company",
            "contact",
            "contactNote",
            "contactTag",
            "ecommerceOrder",
            "ecommerceProduct",
            "email",
            "file"
          ],
          "default": "company"
        },
        "operation": {
          "description": "Delete a file",
          "type": "string",
          "enum": [
            "delete",
            "getAll",
            "upload"
          ],
          "default": "delete"
        },
        "companyName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Email field of each Contact record to address the email to, such as 'EmailAddress1', 'EmailAddress2', 'EmailAddress3', defaulting to the contact's primary email",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "addressesUi": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Address"
          ]
        },
        "faxesUi": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Fax"
          ]
        },
        "phonesUi": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Phone"
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
        "options": {
          "description": "Date to start searching from",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "duplicateOption": {
          "description": "Performs duplicate checking by one of the following options: Email, EmailAndName. If a match is found using the option provided, the existing contact will be updated.",
          "type": "string",
          "enum": [
            "email",
            "emailAndName"
          ],
          "default": "email"
        },
        "emailsUi": {
          "description": "",
          "type": "string",
          "default": {},
          "format": "email",
          "examples": [
            "Add Email"
          ]
        },
        "socialAccountsUi": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Social Account"
          ]
        },
        "contactId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "userId": {
          "description": "The infusionsoft user to send the email on behalf of. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": ""
        },
        "noteId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "filters": {
          "description": "Filter based on Contact ID, if user has permission to see Contact files",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "tagIds": {
          "description": "",
          "type": "string",
          "default": "Tag IDs, multiple IDs can be set separated by comma."
        },
        "orderDate": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "orderTitle": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "orderType": {
          "description": "",
          "type": "string",
          "enum": [
            "offline",
            "online"
          ],
          "default": ""
        },
        "addressUi": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Address"
          ]
        },
        "orderItemsUi": {
          "description": "Overridable price of the product, if not specified, the default will be used",
          "type": "string",
          "default": {},
          "examples": [
            "Add Order Item"
          ]
        },
        "orderId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "productName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "productId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "sentToAddress": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "sentFromAddress": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "contactIds": {
          "description": "Contact IDs to receive the email. Multiple can be added seperated by comma.",
          "type": "string",
          "default": ""
        },
        "subject": {
          "description": "The subject line of the email",
          "type": "string",
          "default": ""
        },
        "attachmentsUi": {
          "description": "The content of the attachment, encoded in Base64",
          "type": "string",
          "default": "",
          "examples": [
            "Add Attachments"
          ]
        },
        "binaryData": {
          "description": "Whether the data to upload should be taken from binary field",
          "type": "boolean",
          "default": false
        },
        "binaryPropertyName": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "fileAssociation": {
          "description": "",
          "type": "string",
          "enum": [
            "company",
            "contact",
            "user"
          ],
          "default": ""
        },
        "fileName": {
          "description": "The filename of the attached file, including extension",
          "type": "string",
          "default": ""
        },
        "fileData": {
          "description": "The content of the attachment, encoded in Base64",
          "type": "string",
          "default": ""
        },
        "isPublic": {
          "description": "",
          "type": "boolean",
          "default": false
        },
        "fileId": {
          "description": "",
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
      "name": "keapOAuth2Api",
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
