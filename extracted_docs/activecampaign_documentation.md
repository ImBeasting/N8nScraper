---
title: "Node: ActiveCampaign"
slug: "node-activecampaign"
version: "1"
updated: "2025-11-13"
summary: "Create and edit data in ActiveCampaign"
node_type: "regular"
group: "['transform']"
---

# Node: ActiveCampaign

**Purpose.** Create and edit data in ActiveCampaign
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `{'light': 'file:activeCampaign.svg', 'dark': 'file:activeCampaign.dark.svg'}`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **activeCampaignApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `activeCampaignApi` | ✓ | - |

---

## Operations

### Account Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an account |
| Delete | `delete` | Delete an account |
| Get | `get` | Get data of an account |
| Get Many | `getAll` | Get data of many accounts |
| Update | `update` | Update an account |

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a contact |
| Delete | `delete` | Delete a contact |
| Get | `get` | Get data of a contact |
| Get Many | `getAll` | Get data of many contacts |
| Update | `update` | Update a contact |

### Accountcontact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an association |
| Delete | `delete` | Delete an association |
| Update | `update` | Update an association |

### Contactlist Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add contact to a list |
| Remove | `remove` | Remove contact from a list |

### Contacttag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Add | `add` | Add a tag to a contact |
| Remove | `remove` | Remove a tag from a contact |

### List Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get many lists |

### Tag Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a tag |
| Delete | `delete` | Delete a tag |
| Get | `get` | Get data of a tag |
| Get Many | `getAll` | Get data of many tags |
| Update | `update` | Update a tag |

### Deal Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a deal |
| Create Note | `createNote` | Create a deal note |
| Delete | `delete` | Delete a deal |
| Get | `get` | Get data of a deal |
| Get Many | `getAll` | Get data of many deals |
| Update | `update` | Update a deal |
| Update Deal Note | `updateNote` | Update a deal note |

### Connection Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a connection |
| Delete | `delete` | Delete a connection |
| Get | `get` | Get data of a connection |
| Get Many | `getAll` | Get data of many connections |
| Update | `update` | Update a connection |

### Ecommerceorder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a order |
| Delete | `delete` | Delete a order |
| Get | `get` | Get data of a order |
| Get Many | `getAll` | Get data of many orders |
| Update | `update` | Update a order |

### Ecommercecustomer Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a E-commerce Customer |
| Delete | `delete` | Delete a E-commerce Customer |
| Get | `get` | Get data of a E-commerce Customer |
| Get Many | `getAll` | Get data of many E-commerce Customers |
| Update | `update` | Update a E-commerce Customer |

### Ecommerceorderproducts Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Many | `getAll` | Get data of many order products |
| Get by Product ID | `getByProductId` | Get data of a ordered product |
| Get by Order ID | `getByOrderId` | Get data of an order's products |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | contact | ✗ | Resource to operate on |  |

**Resource options:**

* **Account** (`account`)
* **Account Contact** (`accountContact`)
* **Connection** (`connection`)
* **Contact** (`contact`)
* **Contact List** (`contactList`)
* **Contact Tag** (`contactTag`)
* **Deal** (`deal`)
* **E-Commerce Customer** (`ecommerceCustomer`)
* **E-Commerce Order** (`ecommerceOrder`)
* **E-Commerce Order Product** (`ecommerceOrderProducts`)
* **List** (`list`)
* **Tag** (`tag`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create an account |  |

**Operation options:**

* **Create** (`create`) - Create an account
* **Delete** (`delete`) - Delete an account
* **Get** (`get`) - Get data of an account
* **Get Many** (`getAll`) - Get data of many accounts
* **Update** (`update`) - Update an account

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Type | `tagType` | options | contact | ✓ | Tag contact |  |

**Type options:**

* **Contact** (`contact`) - Tag contact
* **Template** (`template`) - Tag template

| Name | `name` | string |  | ✓ | Name of the new tag |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Description of the new tag | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | Description of the new tag |

</details>

| Name | `name` | string |  | ✓ | Account's name |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Account's website | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account URL | `accountUrl` | string |  | Account's website |
| Fields | `fields` | fixedCollection | {} | Adds a custom fields to set also values which have not been predefined |

</details>

| Account ID | `account` | number |  | ✓ |  |  |
| Contact ID | `contact` | number |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Job Title of the contact at the account | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Job Title | `jobTitle` | string |  | Job Title of the contact at the account |

</details>

| Email | `email` | string |  | ✓ | The email of the contact to create | e.g. name@email.com | email |
| Update if Exists | `updateIfExists` | boolean | False | ✗ | Whether to update user if it exists already. If not set and user exists it will error instead. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Adds a custom fields to set also values which have not been predefined | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Fields | `fieldValues` | fixedCollection | {} | Adds a custom fields to set also values which have not been predefined |
| First Name | `firstName` | string |  | The first name of the contact to create |
| Last Name | `lastName` | string |  | The last name of the contact to create |
| Phone | `phone` | string |  | Phone number of the contact |

</details>

| Title | `title` | string |  | ✓ | The title of the deal |  |
| Deal's Contact ID | `contact` | number | 0 | ✓ | The ID of the deal's contact |  |
| Deal Value | `value` | number | 0 | ✓ | The value of the deal in cents |  |
| Currency | `currency` | options | eur | ✓ | The currency of the deal in 3-character ISO format |  |
| Deal Pipeline ID | `group` | string |  | ✗ | The pipeline ID of the deal |  |
| Deal Stage ID | `stage` | string |  | ✗ | The stage ID of the deal |  |
| Deal Owner ID | `owner` | string |  | ✗ | The owner ID of the deal |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | The description of the deal | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Description | `description` | string |  | The description of the deal |
| Deal Percentage | `percent` | number | 0 | The percentage of the deal |
| Deal Status | `status` | number | 0 | The status of the deal |

</details>

| Service | `service` | string |  | ✓ | The name of the service |  |
| External Account ID | `externalid` | string |  | ✓ | The ID of the account in the external service |  |
| Account Name | `name` | string |  | ✓ | The name associated with the account in the external service. Often this will be a company name (e.g., "My Toystore, Inc."). |  |
| Logo URL | `logoUrl` | string |  | ✓ | The URL to a logo image for the external service | url |
| Link URL | `linkUrl` | string |  | ✓ | The URL to a page where the integration with the external service can be managed in the third-party's website | url |
| External ID | `externalid` | string |  | ✗ | The ID of the order in the external service. ONLY REQUIRED IF EXTERNALCHECKOUTID NOT INCLUDED. |  |
| External Checkout ID | `externalcheckoutid` | string |  | ✗ | The ID of the cart in the external service. ONLY REQUIRED IF EXTERNALID IS NOT INCLUDED. |  |
| Order Source | `source` | number | 0 | ✓ | The order source code (0 - will not trigger automations, 1 - will trigger automations) |  |
| Customer Email | `email` | string |  | ✓ | The email address of the customer who placed the order | e.g. name@email.com | email |
| Total Price | `totalPrice` | number | 0 | ✓ | The total price of the order in cents, including tax and shipping charges. (i.e. $456.78 => 45678). Must be greater than or equal to zero. |  |
| Order Currency | `currency` | options | eur | ✓ | The currency of the order (3-digit ISO code, e.g., "USD") |  |
| Connection ID | `connectionid` | number | 0 | ✓ | The ID of the connection from which this order originated |  |
| Customer ID | `customerid` | number | 0 | ✓ | The ID of the customer associated with this order |  |
| Creation Date | `externalCreatedDate` | dateTime |  | ✓ | The date the order was placed |  |
| Abandoning Date | `abandonedDate` | dateTime |  | ✗ | The date the cart was abandoned. REQUIRED ONLY IF INCLUDING EXTERNALCHECKOUTID. |  |
| Products | `orderProducts` | collection | {} | ✗ | All ordered products | e.g. Add product field |  |

<details>
<summary><strong>Products sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | The name of the product |
| Price | `price` | number | 0 | The price of the product, in cents. (i.e. $456.78 => 45678). Must be greater than or equal to zero. |
| Product Quantity | `quantity` | number | 0 | The quantity ordered |
| Product External ID | `externalid` | string |  | The ID of the product in the external service |
| Product Category | `category` | string |  | The category of the product |
| SKU | `sku` | string |  | The SKU for the product |
| Description | `description` | string |  | The description of the product |
| Image URL | `imageUrl` | string |  | An Image URL that displays an image of the product |
| Product URL | `productUrl` | string |  | A URL linking to the product in your store |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | The total shipping amount for the order in cents | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Shipping Amount | `shippingAmount` | number | 0 | The total shipping amount for the order in cents |
| Tax Amount | `taxAmount` | number | 0 | The total tax amount for the order in cents |
| Discount Amount | `discountAmount` | number | 0 | The total discount amount for the order in cents |
| Order URL | `orderUrl` | string |  | The URL for the order in the external service |
| External Updated Date | `externalUpdatedDate` | dateTime |  | The date the order was updated |
| Shipping Method | `shippingMethod` | string |  | The shipping method of the order |
| Order Number | `orderNumber` | string |  | The order number. This can be different than the externalid. |

</details>

| Service ID | `connectionid` | string |  | ✓ | The ID of the connection object for the service where the customer originates |  |
| Customer ID | `externalid` | string |  | ✓ | The ID of the customer in the external service |  |
| Customer Email | `email` | string |  | ✓ | The email address of the customer | e.g. name@email.com | email |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Whether customer has opt-ed in to marketing communications | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Accepts Marketing | `acceptsMarketing` | boolean | False | Whether customer has opt-ed in to marketing communications |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Tag ID | `tagId` | number | 0 | ✓ | ID of the tag to delete |  |
| Account ID | `accountId` | number | 0 | ✓ | ID of the account to delete |  |
| Account Contact ID | `accountContactId` | number | 0 | ✓ | ID of the account contact to delete |  |
| Contact ID | `contactId` | number | 0 | ✓ | ID of the contact to delete |  |
| Deal ID | `dealId` | number | 0 | ✓ | The ID of the deal to delete |  |
| Connection ID | `connectionId` | number | 0 | ✓ | ID of the connection to delete |  |
| Order ID | `orderId` | number | 0 | ✗ | The ID of the e-commerce order |  |
| Customer ID | `ecommerceCustomerId` | number | 0 | ✓ | ID of the E-commerce customer to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Tag ID | `tagId` | number | 0 | ✓ | ID of the tag to get |  |
| Account ID | `accountId` | number | 0 | ✓ | ID of the account to get |  |
| Contact ID | `contactId` | number | 0 | ✓ | ID of the contact to get |  |
| Deal ID | `dealId` | number | 0 | ✓ | The ID of the deal to get |  |
| Connection ID | `connectionId` | number | 0 | ✓ | ID of the connection to get |  |
| Order ID | `orderId` | number | 0 | ✗ | The ID of the e-commerce order |  |
| Customer ID | `ecommerceCustomerId` | number | 0 | ✓ | ID of the E-commerce customer to get |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Filters | `filters` | collection | {} | ✗ | Search by name | e.g. Add Filter |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Search | `search` | string |  | Search by name |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Contacts created on the specified date | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Datetime | `datetime` | dateTime |  | Contacts created on the specified date |
| Email | `email` | string |  | Email address of the contact you want to get |
| Email Like | `email_like` | string |  | Filter contacts that contain the given value in the email address |
| Exclude | `exclude` | string |  | Exclude from the response the contact with the given ID |
| Form ID | `formid` | string |  | Filter contacts associated with the given form |
| List ID | `listid` | string |  | Filter contacts associated with the given list |
| Search | `search` | string |  | Filter contacts that match the given value in the contact names, organization, phone or email |
| Segment ID | `segmentid` | string |  | Return only contacts that match a list segment |
| Series ID | `seriesid` | string |  | Filter contacts associated with the given automation |
| Status | `status` | options |  |  |
| Tag ID | `tagid` | string |  | Filter contacts associated with the given tag |
| Created Before | `filters[created_before]` | dateTime |  | Filter contacts that were created prior to this date |
| Created After | `filters[created_after]` | dateTime |  | Filter contacts that were created after this date |
| Updated Before | `filters[updated_before]` | dateTime |  | Filter contacts that were updated before this date |
| Updated After | `filters[updated_after]` | dateTime |  | Filter contacts that were updated after this date |
| Wait ID | `waitid` | string |  | Filter by contacts in the wait queue of an automation block |
| Order By | `orderBy` | options |  | Order contacts by creation date |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Tag ID | `tagId` | number | 0 | ✓ | ID of the tag to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The fields to update | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Tag | `tag` | string |  | Name of the contact |
| Description | `description` | string |  | Description of the tag being updated |

</details>

| Account ID | `accountId` | number | 0 | ✓ | ID of the account to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The fields to update | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Name | `name` | string |  | Account's name |
| Account URL | `accountUrl` | string |  | Account's website |
| Fields | `fields` | fixedCollection | {} | Adds a custom fields to set also values which have not been predefined |

</details>

| Account Contact ID | `accountContactId` | number |  | ✓ | Account ID |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The fields to update | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Job Title | `jobTitle` | string |  | Job Title of the contact at the account |

</details>

| Contact ID | `contactId` | number | 0 | ✓ | ID of the contact to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The fields to update | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Custom Fields | `fieldValues` | fixedCollection | {} | Adds a custom fields to set also values which have not been predefined |
| Email | `email` | string |  | Email of the contact |
| First Name | `firstName` | string |  | First name of the contact |
| Last Name | `lastName` | string |  | Last name of the contact |
| Phone | `phone` | string |  | Phone number of the contact |

</details>

| Deal ID | `dealId` | number | 0 | ✓ | ID of the deal to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The fields to update | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Title | `title` | string |  | The title of the deal |
| Deal's Contact ID | `contact` | number | 0 | The ID of the deal's contact |
| Deal Value | `value` | number | 0 | The value of the deal in cents |
| Currency | `currency` | options | eur | The currency of the deal in 3-character ISO format |
| Description | `description` | string |  | The description of the deal |
| Deal Pipeline ID | `group` | string |  | The pipeline ID of the deal |
| Deal Stage ID | `stage` | string |  | The stage ID of the deal |
| Deal Owner ID | `owner` | string |  | The owner ID of the deal |
| Deal Percentage | `percent` | number | 0 | The percentage of the deal |
| Deal Status | `status` | number | 0 | The status of the deal |

</details>

| Connection ID | `connectionId` | number | 0 | ✓ | ID of the connection to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The fields to update | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Service | `service` | string |  | The name of the service |
| External Account ID | `externalid` | string |  | The ID of the account in the external service |
| Account Name | `name` | string |  | The name associated with the account in the external service. Often this will be a company name (e.g., "My Toystore, Inc."). |
| Logo URL | `logoUrl` | string |  | The URL to a logo image for the external service |
| Link URL | `linkUrl` | string |  | The URL to a page where the integration with the external service can be managed in the third-party's website |
| Status | `status` | number | 1 | The status of the connection (0 = error; 1 = connected) |
| Syncronisation Status | `syncStatus` | number | 1 | The status of a sync triggered on the connection (0 = sync stopped; 1 = sync running) |

</details>

| Order ID | `orderId` | number | 0 | ✗ | The ID of the e-commerce order |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The ID of the order in the external service. ONLY REQUIRED IF EXTERNALCHECKOUTID NOT INCLUDED. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| External ID | `externalid` | string |  | The ID of the order in the external service. ONLY REQUIRED IF EXTERNALCHECKOUTID NOT INCLUDED. |
| External Checkout ID | `externalcheckoutid` | string |  | The ID of the cart in the external service. ONLY REQUIRED IF EXTERNALID IS NOT INCLUDED. |
| Order Source | `source` | number | 0 | The order source code (0 - will not trigger automations, 1 - will trigger automations) |
| Customer Email | `email` | string |  | The email address of the customer who placed the order |
| Total Price | `totalPrice` | number | 0 | The total price of the order in cents, including tax and shipping charges. (i.e. $456.78 => 45678). Must be greater than or equal to zero. |
| Order Currency | `currency` | options | eur | The currency of the order (3-digit ISO code, e.g., "USD") |
| Connection ID | `connectionid` | number | 0 | The ID of the connection from which this order originated |
| Customer ID | `customerid` | number | 0 | The ID of the customer associated with this order |
| Creation Date | `externalupdatedDate` | dateTime |  | The date the order was placed |
| Abandoning Date | `abandonedDate` | dateTime |  | The date the cart was abandoned. REQUIRED ONLY IF INCLUDING EXTERNALCHECKOUTID. |
| Shipping Amount | `shippingAmount` | number | 0 | The total shipping amount for the order in cents |
| Tax Amount | `taxAmount` | number | 0 | The total tax amount for the order in cents |
| Discount Amount | `discountAmount` | number | 0 | The total discount amount for the order in cents |
| Order URL | `orderUrl` | string |  | The URL for the order in the external service |
| External Updated Date | `externalUpdatedDate` | dateTime |  | The date the order was updated |
| Shipping Method | `shippingMethod` | string |  | The shipping method of the order |
| Order Number | `orderNumber` | string |  | The order number. This can be different than the externalid. |
| Products | `orderProducts` | collection | {} | All ordered products |

</details>

| Customer ID | `ecommerceCustomerId` | number | 0 | ✓ | ID of the E-commerce customer to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | The fields to update | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Service ID | `connectionid` | string |  | The ID of the connection object for the service where the customer originates |
| Customer ID | `externalid` | string |  | The ID of the customer in the external service |
| Customer Email | `email` | string |  | The email address of the customer |
| Accepts Marketing | `acceptsMarketing` | boolean | False | Whether customer has opt-ed in to marketing communications |

</details>


### Add parameters (`add`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Tag Name or ID | `tagId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Contact ID | `contactId` | number |  | ✓ |  |  |
| List ID | `listId` | number |  | ✓ |  |  |
| Contact ID | `contactId` | number |  | ✓ |  |  |

### Remove parameters (`remove`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Contact Tag ID | `contactTagId` | number | 0 | ✓ | ID of the contact tag to delete |  |
| List ID | `listId` | number |  | ✓ |  |  |
| Contact ID | `contactId` | number |  | ✓ |  |  |

### Create Note parameters (`createNote`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Deal ID | `dealId` | number |  | ✓ | The ID of the deal note |  |
| Deal Note | `dealNote` | string |  | ✓ | The content of the deal note |  |

### Update Deal Note parameters (`updateNote`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Deal ID | `dealId` | number |  | ✓ | The ID of the deal note |  |
| Deal Note ID | `dealNoteId` | number |  | ✓ | The ID of the deal note |  |
| Deal Note | `dealNote` | string |  | ✗ | The content of the deal note |  |

### Get by Product ID parameters (`getByProductId`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Product ID | `procuctId` | number | 0 | ✗ | The ID of the product you'd like returned |  |

### Get by Order ID parameters (`getByOrderId`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Order ID | `orderId` | number | 0 | ✗ | The ID of the order whose products you'd like returned |  |

---

## Load Options Methods

- `getContactCustomFields`

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
* Categories: Marketing

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: activeCampaign
displayName: ActiveCampaign
description: Create and edit data in ActiveCampaign
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: activeCampaignApi
  required: true
operations:
- id: create
  name: Create
  description: Create an account
  params:
  - id: tagType
    name: Type
    type: options
    default: contact
    required: true
    description: Tag contact
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - tag
    typeInfo:
      type: options
      displayName: Type
      name: tagType
      possibleValues:
      - value: contact
        name: Contact
        description: Tag contact
      - value: template
        name: Template
        description: Tag template
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Name of the new tag
    validation: &id001
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - connection
    typeInfo: &id002
      type: string
      displayName: Account Name
      name: name
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Account's name
    validation: *id001
    typeInfo: *id002
  - id: account
    name: Account ID
    type: number
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
          - accountContact
    typeInfo:
      type: number
      displayName: Account ID
      name: account
  - id: contact
    name: Contact ID
    type: number
    default: ''
    required: true
    description: ''
    validation: &id003
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - deal
    typeInfo: &id004
      type: number
      displayName: Deal's Contact ID
      name: contact
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email of the contact to create
    placeholder: name@email.com
    validation: &id007
      required: true
      format: email
      displayOptions:
        show:
          operation:
          - create
          resource:
          - ecommerceCustomer
    typeInfo: &id008
      type: string
      displayName: Customer Email
      name: email
  - id: updateIfExists
    name: Update if Exists
    type: boolean
    default: false
    required: false
    description: Whether to update user if it exists already. If not set and user
      exists it will error instead.
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - contact
    typeInfo:
      type: boolean
      displayName: Update if Exists
      name: updateIfExists
  - id: title
    name: Title
    type: string
    default: ''
    required: true
    description: The title of the deal
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - deal
    typeInfo:
      type: string
      displayName: Title
      name: title
  - id: contact
    name: Deal's Contact ID
    type: number
    default: 0
    required: true
    description: The ID of the deal's contact
    validation: *id003
    typeInfo: *id004
  - id: value
    name: Deal Value
    type: number
    default: 0
    required: true
    description: The value of the deal in cents
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - deal
    typeInfo:
      type: number
      displayName: Deal Value
      name: value
  - id: currency
    name: Currency
    type: options
    default: eur
    required: true
    description: The currency of the deal in 3-character ISO format
    validation: &id009
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - ecommerceOrder
    typeInfo: &id010
      type: options
      displayName: Order Currency
      name: currency
      possibleValues: []
  - id: group
    name: Deal Pipeline ID
    type: string
    default: ''
    required: false
    description: The pipeline ID of the deal
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - deal
    typeInfo:
      type: string
      displayName: Deal Pipeline ID
      name: group
  - id: stage
    name: Deal Stage ID
    type: string
    default: ''
    required: false
    description: The stage ID of the deal
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - deal
    typeInfo:
      type: string
      displayName: Deal Stage ID
      name: stage
  - id: owner
    name: Deal Owner ID
    type: string
    default: ''
    required: false
    description: The owner ID of the deal
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - deal
    typeInfo:
      type: string
      displayName: Deal Owner ID
      name: owner
  - id: service
    name: Service
    type: string
    default: ''
    required: true
    description: The name of the service
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - connection
    typeInfo:
      type: string
      displayName: Service
      name: service
  - id: externalid
    name: External Account ID
    type: string
    default: ''
    required: true
    description: The ID of the account in the external service
    validation: &id005
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - ecommerceCustomer
    typeInfo: &id006
      type: string
      displayName: Customer ID
      name: externalid
  - id: name
    name: Account Name
    type: string
    default: ''
    required: true
    description: The name associated with the account in the external service. Often
      this will be a company name (e.g., "My Toystore, Inc.").
    validation: *id001
    typeInfo: *id002
  - id: logoUrl
    name: Logo URL
    type: string
    default: ''
    required: true
    description: The URL to a logo image for the external service
    validation:
      required: true
      format: url
      displayOptions:
        show:
          operation:
          - create
          resource:
          - connection
    typeInfo:
      type: string
      displayName: Logo URL
      name: logoUrl
  - id: linkUrl
    name: Link URL
    type: string
    default: ''
    required: true
    description: The URL to a page where the integration with the external service
      can be managed in the third-party's website
    validation:
      required: true
      format: url
      displayOptions:
        show:
          operation:
          - create
          resource:
          - connection
    typeInfo:
      type: string
      displayName: Link URL
      name: linkUrl
  - id: externalid
    name: External ID
    type: string
    default: ''
    required: false
    description: The ID of the order in the external service. ONLY REQUIRED IF EXTERNALCHECKOUTID
      NOT INCLUDED.
    validation: *id005
    typeInfo: *id006
  - id: externalcheckoutid
    name: External Checkout ID
    type: string
    default: ''
    required: false
    description: The ID of the cart in the external service. ONLY REQUIRED IF EXTERNALID
      IS NOT INCLUDED.
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - ecommerceOrder
    typeInfo:
      type: string
      displayName: External Checkout ID
      name: externalcheckoutid
  - id: source
    name: Order Source
    type: number
    default: 0
    required: true
    description: The order source code (0 - will not trigger automations, 1 - will
      trigger automations)
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - ecommerceOrder
    typeInfo:
      type: number
      displayName: Order Source
      name: source
  - id: email
    name: Customer Email
    type: string
    default: ''
    required: true
    description: The email address of the customer who placed the order
    placeholder: name@email.com
    validation: *id007
    typeInfo: *id008
  - id: totalPrice
    name: Total Price
    type: number
    default: 0
    required: true
    description: The total price of the order in cents, including tax and shipping
      charges. (i.e. $456.78 => 45678). Must be greater than or equal to zero.
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - ecommerceOrder
    typeInfo:
      type: number
      displayName: Total Price
      name: totalPrice
  - id: currency
    name: Order Currency
    type: options
    default: eur
    required: true
    description: The currency of the order (3-digit ISO code, e.g., "USD")
    validation: *id009
    typeInfo: *id010
  - id: connectionid
    name: Connection ID
    type: number
    default: 0
    required: true
    description: The ID of the connection from which this order originated
    validation: &id011
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - ecommerceCustomer
    typeInfo: &id012
      type: string
      displayName: Service ID
      name: connectionid
  - id: customerid
    name: Customer ID
    type: number
    default: 0
    required: true
    description: The ID of the customer associated with this order
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - create
          resource:
          - ecommerceOrder
    typeInfo:
      type: number
      displayName: Customer ID
      name: customerid
  - id: externalCreatedDate
    name: Creation Date
    type: dateTime
    default: ''
    required: true
    description: The date the order was placed
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
      displayName: Creation Date
      name: externalCreatedDate
  - id: abandonedDate
    name: Abandoning Date
    type: dateTime
    default: ''
    required: false
    description: The date the cart was abandoned. REQUIRED ONLY IF INCLUDING EXTERNALCHECKOUTID.
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - ecommerceOrder
    typeInfo:
      type: dateTime
      displayName: Abandoning Date
      name: abandonedDate
  - id: connectionid
    name: Service ID
    type: string
    default: ''
    required: true
    description: The ID of the connection object for the service where the customer
      originates
    validation: *id011
    typeInfo: *id012
  - id: externalid
    name: Customer ID
    type: string
    default: ''
    required: true
    description: The ID of the customer in the external service
    validation: *id005
    typeInfo: *id006
  - id: email
    name: Customer Email
    type: string
    default: ''
    required: true
    description: The email address of the customer
    placeholder: name@email.com
    validation: *id007
    typeInfo: *id008
- id: delete
  name: Delete
  description: Delete an account
  params:
  - id: tagId
    name: Tag ID
    type: number
    default: 0
    required: true
    description: ID of the tag to delete
    validation: &id013
      required: true
      displayOptions:
        show:
          operation:
          - add
          resource:
          - contactTag
    typeInfo: &id014
      type: options
      displayName: Tag Name or ID
      name: tagId
      typeOptions:
        loadOptionsMethod: getTags
      possibleValues: []
  - id: accountId
    name: Account ID
    type: number
    default: 0
    required: true
    description: ID of the account to delete
    validation: &id015
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - account
    typeInfo: &id016
      type: number
      displayName: Account ID
      name: accountId
  - id: accountContactId
    name: Account Contact ID
    type: number
    default: 0
    required: true
    description: ID of the account contact to delete
    validation: &id027
      required: true
      displayOptions:
        show:
          operation:
          - update
          resource:
          - accountContact
    typeInfo: &id028
      type: number
      displayName: Account Contact ID
      name: accountContactId
  - id: contactId
    name: Contact ID
    type: number
    default: 0
    required: true
    description: ID of the contact to delete
    validation: &id017
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - contact
    typeInfo: &id018
      type: number
      displayName: Contact ID
      name: contactId
  - id: dealId
    name: Deal ID
    type: number
    default: 0
    required: true
    description: The ID of the deal to delete
    validation: &id019
      required: true
      displayOptions:
        show:
          operation:
          - updateNote
          resource:
          - deal
    typeInfo: &id020
      type: number
      displayName: Deal ID
      name: dealId
  - id: connectionId
    name: Connection ID
    type: number
    default: 0
    required: true
    description: ID of the connection to delete
    validation: &id021
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - connection
    typeInfo: &id022
      type: number
      displayName: Connection ID
      name: connectionId
  - id: orderId
    name: Order ID
    type: number
    default: 0
    required: false
    description: The ID of the e-commerce order
    validation: &id023
      displayOptions:
        show:
          operation:
          - getByOrderId
          resource:
          - ecommerceOrderProducts
    typeInfo: &id024
      type: number
      displayName: Order ID
      name: orderId
  - id: ecommerceCustomerId
    name: Customer ID
    type: number
    default: 0
    required: true
    description: ID of the E-commerce customer to delete
    validation: &id025
      required: true
      displayOptions:
        show:
          operation:
          - get
          resource:
          - ecommerceCustomer
    typeInfo: &id026
      type: number
      displayName: Customer ID
      name: ecommerceCustomerId
- id: get
  name: Get
  description: Get data of an account
  params:
  - id: tagId
    name: Tag ID
    type: number
    default: 0
    required: true
    description: ID of the tag to get
    validation: *id013
    typeInfo: *id014
  - id: accountId
    name: Account ID
    type: number
    default: 0
    required: true
    description: ID of the account to get
    validation: *id015
    typeInfo: *id016
  - id: contactId
    name: Contact ID
    type: number
    default: 0
    required: true
    description: ID of the contact to get
    validation: *id017
    typeInfo: *id018
  - id: dealId
    name: Deal ID
    type: number
    default: 0
    required: true
    description: The ID of the deal to get
    validation: *id019
    typeInfo: *id020
  - id: connectionId
    name: Connection ID
    type: number
    default: 0
    required: true
    description: ID of the connection to get
    validation: *id021
    typeInfo: *id022
  - id: orderId
    name: Order ID
    type: number
    default: 0
    required: false
    description: The ID of the e-commerce order
    validation: *id023
    typeInfo: *id024
  - id: ecommerceCustomerId
    name: Customer ID
    type: number
    default: 0
    required: true
    description: ID of the E-commerce customer to get
    validation: *id025
    typeInfo: *id026
- id: getAll
  name: Get Many
  description: Get data of many accounts
  params: []
- id: update
  name: Update
  description: Update an account
  params:
  - id: tagId
    name: Tag ID
    type: number
    default: 0
    required: true
    description: ID of the tag to update
    validation: *id013
    typeInfo: *id014
  - id: accountId
    name: Account ID
    type: number
    default: 0
    required: true
    description: ID of the account to update
    validation: *id015
    typeInfo: *id016
  - id: accountContactId
    name: Account Contact ID
    type: number
    default: ''
    required: true
    description: Account ID
    validation: *id027
    typeInfo: *id028
  - id: contactId
    name: Contact ID
    type: number
    default: 0
    required: true
    description: ID of the contact to update
    validation: *id017
    typeInfo: *id018
  - id: dealId
    name: Deal ID
    type: number
    default: 0
    required: true
    description: ID of the deal to update
    validation: *id019
    typeInfo: *id020
  - id: connectionId
    name: Connection ID
    type: number
    default: 0
    required: true
    description: ID of the connection to update
    validation: *id021
    typeInfo: *id022
  - id: orderId
    name: Order ID
    type: number
    default: 0
    required: false
    description: The ID of the e-commerce order
    validation: *id023
    typeInfo: *id024
  - id: ecommerceCustomerId
    name: Customer ID
    type: number
    default: 0
    required: true
    description: ID of the E-commerce customer to update
    validation: *id025
    typeInfo: *id026
- id: add
  name: Add
  description: Add contact to a list
  params:
  - id: tagId
    name: Tag Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id013
    typeInfo: *id014
  - id: contactId
    name: Contact ID
    type: number
    default: ''
    required: true
    description: ''
    validation: *id017
    typeInfo: *id018
  - id: listId
    name: List ID
    type: number
    default: ''
    required: true
    description: ''
    validation: &id029
      required: true
      displayOptions:
        show:
          operation:
          - remove
          resource:
          - contactList
    typeInfo: &id030
      type: number
      displayName: List ID
      name: listId
  - id: contactId
    name: Contact ID
    type: number
    default: ''
    required: true
    description: ''
    validation: *id017
    typeInfo: *id018
- id: remove
  name: Remove
  description: Remove contact from a list
  params:
  - id: contactTagId
    name: Contact Tag ID
    type: number
    default: 0
    required: true
    description: ID of the contact tag to delete
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - remove
          resource:
          - contactTag
    typeInfo:
      type: number
      displayName: Contact Tag ID
      name: contactTagId
  - id: listId
    name: List ID
    type: number
    default: ''
    required: true
    description: ''
    validation: *id029
    typeInfo: *id030
  - id: contactId
    name: Contact ID
    type: number
    default: ''
    required: true
    description: ''
    validation: *id017
    typeInfo: *id018
- id: createNote
  name: Create Note
  description: Create a deal note
  params:
  - id: dealId
    name: Deal ID
    type: number
    default: ''
    required: true
    description: The ID of the deal note
    validation: *id019
    typeInfo: *id020
  - id: dealNote
    name: Deal Note
    type: string
    default: ''
    required: true
    description: The content of the deal note
    validation: &id031
      displayOptions:
        show:
          operation:
          - updateNote
          resource:
          - deal
    typeInfo: &id032
      type: string
      displayName: Deal Note
      name: dealNote
- id: updateNote
  name: Update Deal Note
  description: Update a deal note
  params:
  - id: dealId
    name: Deal ID
    type: number
    default: ''
    required: true
    description: The ID of the deal note
    validation: *id019
    typeInfo: *id020
  - id: dealNoteId
    name: Deal Note ID
    type: number
    default: ''
    required: true
    description: The ID of the deal note
    validation:
      required: true
      displayOptions:
        show:
          operation:
          - updateNote
          resource:
          - deal
    typeInfo:
      type: number
      displayName: Deal Note ID
      name: dealNoteId
  - id: dealNote
    name: Deal Note
    type: string
    default: ''
    required: false
    description: The content of the deal note
    validation: *id031
    typeInfo: *id032
- id: getByProductId
  name: Get by Product ID
  description: Get data of a ordered product
  params:
  - id: procuctId
    name: Product ID
    type: number
    default: 0
    required: false
    description: The ID of the product you'd like returned
    validation:
      displayOptions:
        show:
          operation:
          - getByProductId
          resource:
          - ecommerceOrderProducts
    typeInfo:
      type: number
      displayName: Product ID
      name: procuctId
- id: getByOrderId
  name: Get by Order ID
  description: Get data of an order's products
  params:
  - id: orderId
    name: Order ID
    type: number
    default: 0
    required: false
    description: The ID of the order whose products you'd like returned
    validation: *id023
    typeInfo: *id024
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
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: filters
    text: Add Filter
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: email
    text: name@email.com
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
  - field: updateFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: orderProducts
    text: Add product field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: email
    text: name@email.com
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/activeCampaign.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "ActiveCampaign Node",
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
        "add",
        "remove",
        "createNote",
        "updateNote",
        "getByProductId",
        "getByOrderId"
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
            "accountContact",
            "connection",
            "contact",
            "contactList",
            "contactTag",
            "deal",
            "ecommerceCustomer",
            "ecommerceOrder",
            "ecommerceOrderProducts",
            "list",
            "tag"
          ],
          "default": "contact"
        },
        "operation": {
          "description": "Get data of many order products",
          "type": "string",
          "enum": [
            "getAll",
            "getByProductId",
            "getByOrderId"
          ],
          "default": "getAll"
        },
        "tagType": {
          "description": "Tag contact",
          "type": "string",
          "enum": [
            "contact",
            "template"
          ],
          "default": "contact"
        },
        "name": {
          "description": "The name associated with the account in the external service. Often this will be a company name (e.g., \"My Toystore, Inc.\").",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Whether customer has opt-ed in to marketing communications",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "tagId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "updateFields": {
          "description": "The fields to update",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "contactId": {
          "description": "ID of the contact to get",
          "type": "number",
          "default": 0
        },
        "contactTagId": {
          "description": "ID of the contact tag to delete",
          "type": "number",
          "default": 0
        },
        "listId": {
          "description": "",
          "type": "number",
          "default": ""
        },
        "accountId": {
          "description": "ID of the account to get",
          "type": "number",
          "default": 0
        },
        "filters": {
          "description": "Search by name",
          "type": "string",
          "default": {},
          "examples": [
            "Add Filter"
          ]
        },
        "account": {
          "description": "",
          "type": "number",
          "default": ""
        },
        "contact": {
          "description": "The ID of the deal's contact",
          "type": "number",
          "default": 0
        },
        "accountContactId": {
          "description": "Account ID",
          "type": "number",
          "default": ""
        },
        "email": {
          "description": "The email address of the customer",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "updateIfExists": {
          "description": "Whether to update user if it exists already. If not set and user exists it will error instead.",
          "type": "boolean",
          "default": false
        },
        "title": {
          "description": "The title of the deal",
          "type": "string",
          "default": ""
        },
        "value": {
          "description": "The value of the deal in cents",
          "type": "number",
          "default": 0
        },
        "currency": {
          "description": "The currency of the order (3-digit ISO code, e.g., \"USD\")",
          "type": "string",
          "default": "eur"
        },
        "group": {
          "description": "The pipeline ID of the deal",
          "type": "string",
          "default": ""
        },
        "stage": {
          "description": "The stage ID of the deal",
          "type": "string",
          "default": ""
        },
        "owner": {
          "description": "The owner ID of the deal",
          "type": "string",
          "default": ""
        },
        "dealId": {
          "description": "The ID of the deal note",
          "type": "number",
          "default": ""
        },
        "dealNote": {
          "description": "The content of the deal note",
          "type": "string",
          "default": ""
        },
        "dealNoteId": {
          "description": "The ID of the deal note",
          "type": "number",
          "default": ""
        },
        "service": {
          "description": "The name of the service",
          "type": "string",
          "default": ""
        },
        "externalid": {
          "description": "The ID of the customer in the external service",
          "type": "string",
          "default": ""
        },
        "logoUrl": {
          "description": "The URL to a logo image for the external service",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "linkUrl": {
          "description": "The URL to a page where the integration with the external service can be managed in the third-party's website",
          "type": "string",
          "default": "",
          "format": "url"
        },
        "connectionId": {
          "description": "ID of the connection to get",
          "type": "number",
          "default": 0
        },
        "externalcheckoutid": {
          "description": "The ID of the cart in the external service. ONLY REQUIRED IF EXTERNALID IS NOT INCLUDED.",
          "type": "string",
          "default": ""
        },
        "source": {
          "description": "The order source code (0 - will not trigger automations, 1 - will trigger automations)",
          "type": "number",
          "default": 0
        },
        "totalPrice": {
          "description": "The total price of the order in cents, including tax and shipping charges. (i.e. $456.78 => 45678). Must be greater than or equal to zero.",
          "type": "number",
          "default": 0
        },
        "connectionid": {
          "description": "The ID of the connection object for the service where the customer originates",
          "type": "string",
          "default": ""
        },
        "customerid": {
          "description": "The ID of the customer associated with this order",
          "type": "number",
          "default": 0
        },
        "externalCreatedDate": {
          "description": "The date the order was placed",
          "type": "string",
          "default": ""
        },
        "abandonedDate": {
          "description": "The date the cart was abandoned. REQUIRED ONLY IF INCLUDING EXTERNALCHECKOUTID.",
          "type": "string",
          "default": ""
        },
        "orderProducts": {
          "description": "All ordered products",
          "type": "string",
          "default": {},
          "examples": [
            "Add product field"
          ]
        },
        "orderId": {
          "description": "The ID of the order whose products you'd like returned",
          "type": "number",
          "default": 0
        },
        "ecommerceCustomerId": {
          "description": "ID of the E-commerce customer to get",
          "type": "number",
          "default": 0
        },
        "procuctId": {
          "description": "The ID of the product you'd like returned",
          "type": "number",
          "default": 0
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
      "name": "activeCampaignApi",
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
