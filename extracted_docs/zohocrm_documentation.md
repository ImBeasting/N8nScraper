---
title: "Node: Zoho CRM"
slug: "node-zohocrm"
version: "1"
updated: "2026-01-08"
summary: "Consume Zoho CRM API"
node_type: "regular"
group: "['transform']"
---

# Node: Zoho CRM

**Purpose.** Consume Zoho CRM API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:zoho.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **zohoOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `zohoOAuth2Api` | ✓ | - |

---

## Operations

### Vendor Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a vendor |
| Create or Update | `upsert` | Create a new record, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a vendor |
| Get | `get` | Get a vendor |
| Get Many | `getAll` | Get many vendors |
| Update | `update` | Update a vendor |

### Account Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an account |
| Create or Update | `upsert` | Create a new record, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete an account |
| Get | `get` | Get an account |
| Get Many | `getAll` | Get many accounts |
| Update | `update` | Update an account |

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a contact |
| Create or Update | `upsert` | Create a new record, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a contact |
| Get | `get` | Get a contact |
| Get Many | `getAll` | Get many contacts |
| Update | `update` | Update a contact |

### Deal Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a deal |
| Create or Update | `upsert` | Create a new record, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a contact |
| Get | `get` | Get a contact |
| Get Many | `getAll` | Get many contacts |
| Update | `update` | Update a contact |

### Invoice Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an invoice |
| Create or Update | `upsert` | Create a new record, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete an invoice |
| Get | `get` | Get an invoice |
| Get Many | `getAll` | Get many invoices |
| Update | `update` | Update an invoice |

### Lead Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a lead |
| Create or Update | `upsert` | Create a new record, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a lead |
| Get | `get` | Get a lead |
| Get Fields | `getFields` | Get lead fields |
| Get Many | `getAll` | Get many leads |
| Update | `update` | Update a lead |

### Product Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a product |
| Create or Update | `upsert` | Create a new record, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a product |
| Get | `get` | Get a product |
| Get Many | `getAll` | Get many products |
| Update | `update` | Update a product |

### Purchaseorder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a purchase order |
| Create or Update | `upsert` | Create a new record, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a purchase order |
| Get | `get` | Get a purchase order |
| Get Many | `getAll` | Get many purchase orders |
| Update | `update` | Update a purchase order |

### Quote Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a quote |
| Create or Update | `upsert` | Create a new record, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a quote |
| Get | `get` | Get a quote |
| Get Many | `getAll` | Get many quotes |
| Update | `update` | Update a quote |

### Salesorder Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a sales order |
| Create or Update | `upsert` | Create a new record, or update the current one if it already exists (upsert) |
| Delete | `delete` | Delete a sales order |
| Get | `get` | Get a sales order |
| Get Many | `getAll` | Get many sales orders |
| Update | `update` | Update a sales order |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | account | ✗ | Resource to operate on |  |

**Resource options:**

* **Account** (`account`)
* **Contact** (`contact`)
* **Deal** (`deal`)
* **Invoice** (`invoice`)
* **Lead** (`lead`)
* **Product** (`product`)
* **Purchase Order** (`purchaseOrder`)
* **Quote** (`quote`)
* **Sales Order** (`salesOrder`)
* **Vendor** (`vendor`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a vendor |  |

**Operation options:**

* **Create** (`create`) - Create a vendor
* **Create or Update** (`upsert`) - Create a new record, or update the current one if it already exists (upsert)
* **Delete** (`delete`) - Delete a vendor
* **Get** (`get`) - Get a vendor
* **Get Many** (`getAll`) - Get many vendors
* **Update** (`update`) - Update a vendor

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Vendor Name | `vendorName` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Category | `Category` | string |  |  |
| Currency | `Currency` | options | USD |  |
| Description | `Description` | string |  |  |
| Email | `Email` | string |  |  |
| Phone | `Phone` | string |  |  |
| Website | `Website` | string |  |  |

</details>

| Account Name | `accountName` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Name of the account’s location, e.g. Headquarters or London | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Number | `Account_Number` | string |  |  |
| Account Site | `Account_Site` | string |  | Name of the account’s location, e.g. Headquarters or London |
| Account Type Name or ID | `Account_Type` | options | [] | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Annual Revenue | `Annual_Revenue` | number |  |  |
| Contact Details | `Contact_Details` | string |  |  |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Description | `Description` | string |  |  |
| Employees | `Employees` | number |  | Number of employees in the account’s company |
| Exchange Rate | `Exchange_Rate` | number |  | Exchange rate of the default currency to the home currency |
| Fax | `Fax` | string |  |  |
| Industry | `Industry` | string |  |  |
| Phone | `Phone` | string |  |  |
| Ticker Symbol | `Ticker_Symbol` | string |  |  |
| Website | `Website` | string |  |  |

</details>

| Last Name | `lastName` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Name of the contact’s assistant | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assistant | `Assistant` | string |  | Name of the contact’s assistant |
| Date of Birth | `Date_of_Birth` | dateTime |  |  |
| Department | `Department` | string |  | Company department to which the contact belongs |
| Description | `Description` | string |  |  |
| Email (Primary) | `Email` | string |  |  |
| Email (Secondary) | `Secondary_Email` | string |  |  |
| Fax | `Fax` | string |  |  |
| First Name | `First_Name` | string |  |  |
| Full Name | `Full_Name` | string |  |  |
| Mobile | `Mobile` | string |  |  |
| Phone | `Phone` | string |  |  |
| Phone (Assistant) | `Asst_Phone` | string |  | Phone number of the contact’s assistant |
| Phone (Home) | `Home_Phone` | string |  |  |
| Phone (Other) | `Other_Phone` | string |  |  |
| Salutation | `Salutation` | string |  |  |
| Skype ID | `Skype_ID` | string |  |  |
| Title | `Title` | string |  | Position of the contact at their company |
| Twitter | `Twitter` | string |  |  |

</details>

| Deal Name | `dealName` | string |  | ✓ |  |  |
| Stage Name or ID | `stage` | options | [] | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Monetary amount of the deal | e.g. Add Field | min:0, max:100 |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Amount | `Amount` | number |  | Monetary amount of the deal |
| Closing Date | `Closing_Date` | dateTime |  |  |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Description | `Description` | string |  |  |
| Lead Conversion Time | `Lead_Conversion_Time` | number |  | Average number of days to convert the lead into a deal |
| Next Step | `Next_Step` | string |  | Description of the next step in the sales process |
| Overall Sales Duration | `Overall_Sales_Duration` | number |  | Average number of days to convert the lead into a deal and to win the deal |
| Probability | `Probability` | number |  | Probability of deal closure as a percentage. For example, enter 12 for 12%. |
| Sales Cycle Duration | `Sales_Cycle_Duration` | number | 0 | Average number of days for the deal to be won |

</details>

| Subject | `subject` | string |  | ✓ | Subject or title of the invoice |  |
| Products | `Product_Details` | collection | {} | ✗ | e.g. Add Field |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the account associated with this invoice. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Name or ID | `accountId` | options | [] | ID of the account associated with this invoice. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Adjustment | `Adjustment` | number |  | Adjustment in the grand total, if any |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Description | `Description` | string |  |  |
| Due Date | `Due_Date` | dateTime |  |  |
| Exchange Rate | `Exchange_Rate` | number |  | Exchange rate of the default currency to the home currency |
| Grand Total | `Grand_Total` | number |  | Total amount for the product after deducting tax and discounts |
| Invoice Date | `Invoice_Date` | dateTime |  |  |
| Invoice Number | `Invoice_Number` | string |  |  |
| Sales Commission | `Sales_Commission` | number |  | Commission of sales person on deal closure as a percentage. For example, enter 12 for 12%. |
| Status | `Status` | string |  |  |
| Sub Total | `Sub_Total` | number |  | Total amount for the product excluding tax |
| Tax | `Tax` | number |  | Tax amount as the sum of sales tax and value-added tax |
| Terms and Conditions | `Terms_and_Conditions` | string |  | Terms and conditions associated with the invoice |

</details>

| Company | `Company` | string |  | ✓ | Company at which the lead works |  |
| Last Name | `lastName` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Annual revenue of the lead’s company | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Annual Revenue | `Annual_Revenue` | number |  | Annual revenue of the lead’s company |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Description | `Description` | string |  |  |
| Designation | `Designation` | string |  | Position of the lead at their company |
| Email | `Email` | string |  |  |
| Email Opt Out | `Email_Opt_Out` | boolean | False |  |
| Fax | `Fax` | string |  |  |
| First Name | `First_Name` | string |  |  |
| Full Name | `Full_Name` | string |  |  |
| Industry | `Industry` | string |  | Industry to which the lead belongs |
| Industry Type | `Industry_Type` | string |  | Type of industry to which the lead belongs |
| Lead Source | `Lead_Source` | string |  | Source from which the lead was created |
| Lead Status | `Lead_Status` | string |  |  |
| Mobile | `Mobile` | string |  |  |
| Number of Employees | `No_of_Employees` | number |  | Number of employees in the lead’s company |
| Phone | `Phone` | string |  |  |
| Salutation | `Salutation` | string |  |  |
| Secondary Email | `Secondary_Email` | string |  |  |
| Skype ID | `Skype_ID` | string |  |  |
| Twitter | `Twitter` | string |  |  |
| Website | `Website` | string |  |  |

</details>

| Product Name | `productName` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Commission rate for the product. For example, enter 12 for 12%. | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Commission Rate | `Commission_Rate` | number | 0 | Commission rate for the product. For example, enter 12 for 12%. |
| Description | `Description` | string |  |  |
| Manufacturer | `Manufacturer` | string |  |  |
| Product Active | `Product_Active` | boolean | False |  |
| Product Category | `Product_Category` | string |  |  |
| Quantity in Demand | `Qty_in_Demand` | number | 0 |  |
| Quantity in Stock | `Qty_in_Stock` | number | 0 |  |
| Taxable | `Taxable` | boolean | False |  |
| Unit Price | `Unit_Price` | number | 0 |  |

</details>

| Subject | `subject` | string |  | ✓ | Subject or title of the purchase order |  |
| Vendor Name or ID | `vendorId` | options | [] | ✗ | ID of the vendor associated with the purchase order. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Products | `Product_Details` | collection | {} | ✗ | e.g. Add Field |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Adjustment in the grand total, if any | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Adjustment | `Adjustment` | number | 0 | Adjustment in the grand total, if any |
| Billing Address | `Billing_Address` | fixedCollection | {} |  |
| Carrier | `Carrier` | string |  | Name of the carrier |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Description | `Description` | string |  |  |
| Discount | `Discount` | number | 0 | Discount applied to the purchase order. For example, enter 12 for 12%. |
| Due Date | `Due_Date` | dateTime |  |  |
| Exchange Rate | `Exchange_Rate` | number | 0 | Exchange rate of the default currency to the home currency |
| Grand Total | `Grand_Total` | number | 0 | Total amount for the product after deducting tax and discounts |
| PO Date | `PO_Date` | dateTime |  | Date on which the purchase order was issued |
| PO Number | `PO_Number` | string |  | ID of the purchase order after creating a case |
| Sales Commission | `Sales_Commission` | number | 0 | Commission of sales person on deal closure as a percentage. For example, enter 12 for 12%. |
| Status Name or ID | `Status` | options | [] | Status of the purchase order. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Sub Total | `Sub_Total` | number | 0 | Total amount for the product excluding tax |
| Tax | `Tax` | number | 0 | Tax amount as the sum of sales tax and value-added tax |
| Terms and Conditions | `Terms_and_Conditions` | string |  | Terms and conditions associated with the purchase order |
| Tracking Number | `Tracking_Number` | string |  |  |

</details>

| Subject | `subject` | string |  | ✓ | Subject or title of the quote |  |
| Products | `Product_Details` | collection | {} | ✗ | e.g. Add Field |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Adjustment in the grand total, if any | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Adjustment | `Adjustment` | number | 0 | Adjustment in the grand total, if any |
| Carrier | `Carrier` | string |  |  |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Description | `Description` | string |  |  |
| Exchange Rate | `Exchange_Rate` | number | 0 | Exchange rate of the default currency to the home currency |
| Grand Total | `Grand_Total` | number | 0 | Total amount for the product after deducting tax and discounts |
| Quote Stage Name or ID | `Quote_Stage` | options | [] | Stage of the quote. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Sub Total | `Sub_Total` | number | 0 | Total amount for the product excluding tax |
| Tax | `Tax` | number | 0 | Total amount as the sum of sales tax and value-added tax |
| Team | `Team` | string |  | Team for whom the quote is created |
| Terms and Conditions | `Terms_and_Conditions` | string |  | Terms and conditions associated with the quote |
| Valid Till | `Valid_Till` | dateTime |  | Date until when the quote is valid |

</details>

| Account Name or ID | `accountId` | options | [] | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Subject | `subject` | string |  | ✓ | Subject or title of the sales order |  |
| Products | `Product_Details` | collection | {} | ✗ | e.g. Add Field |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Adjustment in the grand total, if any | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Adjustment | `Adjustment` | number | 0 | Adjustment in the grand total, if any |
| Carrier | `Carrier` | string |  | Name of the carrier |
| Contact Name or ID | `contactId` | options | [] | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Deal Name or ID | `dealId` | options | [] | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Description | `Description` | string |  |  |
| Discount | `Discount` | number | 0 | Discount applied to the sales order. For example, enter 12 for 12%. |
| Due Date | `Due_Date` | dateTime |  |  |
| Exchange Rate | `Exchange_Rate` | number | 0 | Exchange rate of the default currency to the home currency |
| Grand Total | `Grand_Total` | number | 0 | Total amount for the product after deducting tax and discounts |
| Sales Order Number | `SO_Number` | string |  | ID of the sales order after creating a case |
| Sales Commission | `Sales_Commission` | number | 0 | Commission of sales person on deal closure as a percentage. For example, enter 12 for 12%. |
| Status Name or ID | `Status` | options | [] | Status of the sales order. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Sub Total | `Sub_Total` | number | 0 | Total amount for the product excluding tax |
| Tax | `Tax` | number | 0 | Tax amount as the sum of sales tax and value-added tax |
| Terms and Conditions | `Terms_and_Conditions` | string |  | Terms and conditions associated with the purchase order |

</details>


### Create or Update parameters (`upsert`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Vendor Name | `vendorName` | string |  | ✓ | Name of the vendor. If a record with this vendor name exists it will be updated, otherwise a new one will be created. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Category | `Category` | string |  |  |
| Currency | `Currency` | options | USD |  |
| Description | `Description` | string |  |  |
| Email | `Email` | string |  |  |
| Phone | `Phone` | string |  |  |
| Website | `Website` | string |  |  |

</details>

| Account Name | `accountName` | string |  | ✓ | Name of the account. If a record with this account name exists it will be updated, otherwise a new one will be created. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Name of the account’s location, e.g. Headquarters or London | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Number | `Account_Number` | string |  |  |
| Account Site | `Account_Site` | string |  | Name of the account’s location, e.g. Headquarters or London |
| Account Type Name or ID | `Account_Type` | options | [] | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Annual Revenue | `Annual_Revenue` | number |  |  |
| Contact Details | `Contact_Details` | string |  |  |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Description | `Description` | string |  |  |
| Employees | `Employees` | number |  | Number of employees in the account’s company |
| Exchange Rate | `Exchange_Rate` | number |  | Exchange rate of the default currency to the home currency |
| Fax | `Fax` | string |  |  |
| Industry | `Industry` | string |  |  |
| Phone | `Phone` | string |  |  |
| Ticker Symbol | `Ticker_Symbol` | string |  |  |
| Website | `Website` | string |  |  |

</details>

| Last Name | `lastName` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Name of the contact’s assistant | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assistant | `Assistant` | string |  | Name of the contact’s assistant |
| Date of Birth | `Date_of_Birth` | dateTime |  |  |
| Department | `Department` | string |  | Company department to which the contact belongs |
| Description | `Description` | string |  |  |
| Email (Primary) | `Email` | string |  | Email of the contact. If a record with this email exists it will be updated, otherwise a new one will be created. |
| Email (Secondary) | `Secondary_Email` | string |  |  |
| Fax | `Fax` | string |  |  |
| First Name | `First_Name` | string |  |  |
| Full Name | `Full_Name` | string |  |  |
| Mobile | `Mobile` | string |  |  |
| Phone | `Phone` | string |  |  |
| Phone (Assistant) | `Asst_Phone` | string |  | Phone number of the contact’s assistant |
| Phone (Home) | `Home_Phone` | string |  |  |
| Phone (Other) | `Other_Phone` | string |  |  |
| Salutation | `Salutation` | string |  |  |
| Skype ID | `Skype_ID` | string |  |  |
| Title | `Title` | string |  | Position of the contact at their company |
| Twitter | `Twitter` | string |  |  |

</details>

| Deal Name | `dealName` | string |  | ✓ | Name of the deal. If a record with this deal name exists it will be updated, otherwise a new one will be created. |  |
| Stage Name or ID | `stage` | options | [] | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Monetary amount of the deal | e.g. Add Field | min:0, max:100 |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Amount | `Amount` | number |  | Monetary amount of the deal |
| Closing Date | `Closing_Date` | dateTime |  |  |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Description | `Description` | string |  |  |
| Lead Conversion Time | `Lead_Conversion_Time` | number |  | Average number of days to convert the lead into a deal |
| Next Step | `Next_Step` | string |  | Description of the next step in the sales process |
| Overall Sales Duration | `Overall_Sales_Duration` | number |  | Average number of days to convert the lead into a deal and to win the deal |
| Probability | `Probability` | number |  | Probability of deal closure as a percentage. For example, enter 12 for 12%. |
| Sales Cycle Duration | `Sales_Cycle_Duration` | number | 0 | Average number of days for the deal to be won |

</details>

| Subject | `subject` | string |  | ✓ | Subject or title of the invoice. If a record with this subject exists it will be updated, otherwise a new one will be created. |  |
| Products | `Product_Details` | collection | {} | ✗ | e.g. Add Field |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | ID of the account associated with this invoice. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Name or ID | `accountId` | options | [] | ID of the account associated with this invoice. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Adjustment | `Adjustment` | number |  | Adjustment in the grand total, if any |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Description | `Description` | string |  |  |
| Due Date | `Due_Date` | dateTime |  |  |
| Exchange Rate | `Exchange_Rate` | number |  | Exchange rate of the default currency to the home currency |
| Grand Total | `Grand_Total` | number |  | Total amount for the product after deducting tax and discounts |
| Invoice Date | `Invoice_Date` | dateTime |  |  |
| Invoice Number | `Invoice_Number` | string |  |  |
| Sales Commission | `Sales_Commission` | number |  | Commission of sales person on deal closure as a percentage. For example, enter 12 for 12%. |
| Status | `Status` | string |  |  |
| Sub Total | `Sub_Total` | number |  | Total amount for the product excluding tax |
| Tax | `Tax` | number |  | Tax amount as the sum of sales tax and value-added tax |
| Terms and Conditions | `Terms_and_Conditions` | string |  | Terms and conditions associated with the invoice |

</details>

| Company | `Company` | string |  | ✓ | Company at which the lead works |  |
| Last Name | `lastName` | string |  | ✓ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Annual revenue of the lead’s company | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Annual Revenue | `Annual_Revenue` | number |  | Annual revenue of the lead’s company |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Description | `Description` | string |  |  |
| Designation | `Designation` | string |  | Position of the lead at their company |
| Email | `Email` | string |  | Email of the lead. If a record with this email exists it will be updated, otherwise a new one will be created. |
| Email Opt Out | `Email_Opt_Out` | boolean | False |  |
| Fax | `Fax` | string |  |  |
| First Name | `First_Name` | string |  |  |
| Full Name | `Full_Name` | string |  |  |
| Industry | `Industry` | string |  | Industry to which the lead belongs |
| Industry Type | `Industry_Type` | string |  | Type of industry to which the lead belongs |
| Lead Source | `Lead_Source` | string |  | Source from which the lead was created |
| Lead Status | `Lead_Status` | string |  |  |
| Mobile | `Mobile` | string |  |  |
| Number of Employees | `No_of_Employees` | number |  | Number of employees in the lead’s company |
| Phone | `Phone` | string |  |  |
| Salutation | `Salutation` | string |  |  |
| Secondary Email | `Secondary_Email` | string |  |  |
| Skype ID | `Skype_ID` | string |  |  |
| Twitter | `Twitter` | string |  |  |
| Website | `Website` | string |  |  |

</details>

| Product Name | `productName` | string |  | ✓ | Name of the product. If a record with this product name exists it will be updated, otherwise a new one will be created. |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Commission rate for the product. For example, enter 12 for 12%. | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Commission Rate | `Commission_Rate` | number | 0 | Commission rate for the product. For example, enter 12 for 12%. |
| Description | `Description` | string |  |  |
| Manufacturer | `Manufacturer` | string |  |  |
| Product Active | `Product_Active` | boolean | False |  |
| Product Category | `Product_Category` | string |  |  |
| Quantity in Demand | `Qty_in_Demand` | number | 0 |  |
| Quantity in Stock | `Qty_in_Stock` | number | 0 |  |
| Taxable | `Taxable` | boolean | False |  |
| Unit Price | `Unit_Price` | number | 0 |  |

</details>

| Subject | `subject` | string |  | ✓ | Subject or title of the purchase order. If a record with this subject exists it will be updated, otherwise a new one will be created. |  |
| Vendor Name or ID | `vendorId` | options | [] | ✗ | ID of the vendor associated with the purchase order. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Products | `Product_Details` | collection | {} | ✗ | e.g. Add Field |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Adjustment in the grand total, if any | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Adjustment | `Adjustment` | number | 0 | Adjustment in the grand total, if any |
| Billing Address | `Billing_Address` | fixedCollection | {} |  |
| Carrier | `Carrier` | string |  | Name of the carrier |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Description | `Description` | string |  |  |
| Discount | `Discount` | number | 0 | Discount applied to the purchase order. For example, enter 12 for 12%. |
| Due Date | `Due_Date` | dateTime |  |  |
| Exchange Rate | `Exchange_Rate` | number | 0 | Exchange rate of the default currency to the home currency |
| Grand Total | `Grand_Total` | number | 0 | Total amount for the product after deducting tax and discounts |
| PO Date | `PO_Date` | dateTime |  | Date on which the purchase order was issued |
| PO Number | `PO_Number` | string |  | ID of the purchase order after creating a case |
| Sales Commission | `Sales_Commission` | number | 0 | Commission of sales person on deal closure as a percentage. For example, enter 12 for 12%. |
| Status Name or ID | `Status` | options | [] | Status of the purchase order. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Sub Total | `Sub_Total` | number | 0 | Total amount for the product excluding tax |
| Tax | `Tax` | number | 0 | Tax amount as the sum of sales tax and value-added tax |
| Terms and Conditions | `Terms_and_Conditions` | string |  | Terms and conditions associated with the purchase order |
| Tracking Number | `Tracking_Number` | string |  |  |

</details>

| Subject | `subject` | string |  | ✓ | Subject or title of the quote. If a record with this subject exists it will be updated, otherwise a new one will be created. |  |
| Products | `Product_Details` | collection | {} | ✗ | e.g. Add Field |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Adjustment in the grand total, if any | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Adjustment | `Adjustment` | number | 0 | Adjustment in the grand total, if any |
| Carrier | `Carrier` | string |  |  |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Description | `Description` | string |  |  |
| Exchange Rate | `Exchange_Rate` | number | 0 | Exchange rate of the default currency to the home currency |
| Grand Total | `Grand_Total` | number | 0 | Total amount for the product after deducting tax and discounts |
| Quote Stage Name or ID | `Quote_Stage` | options | [] | Stage of the quote. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Sub Total | `Sub_Total` | number | 0 | Total amount for the product excluding tax |
| Tax | `Tax` | number | 0 | Total amount as the sum of sales tax and value-added tax |
| Team | `Team` | string |  | Team for whom the quote is created |
| Terms and Conditions | `Terms_and_Conditions` | string |  | Terms and conditions associated with the quote |
| Valid Till | `Valid_Till` | dateTime |  | Date until when the quote is valid |

</details>

| Account Name or ID | `accountId` | options | [] | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Subject | `subject` | string |  | ✓ | Subject or title of the sales order. If a record with this subject exists it will be updated, otherwise a new one will be created. |  |
| Products | `Product_Details` | collection | {} | ✗ | e.g. Add Field |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | Adjustment in the grand total, if any | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Adjustment | `Adjustment` | number | 0 | Adjustment in the grand total, if any |
| Carrier | `Carrier` | string |  | Name of the carrier |
| Contact Name or ID | `contactId` | options | [] | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Deal Name or ID | `dealId` | options | [] | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Description | `Description` | string |  |  |
| Discount | `Discount` | number | 0 | Discount applied to the sales order. For example, enter 12 for 12%. |
| Due Date | `Due_Date` | dateTime |  |  |
| Exchange Rate | `Exchange_Rate` | number | 0 | Exchange rate of the default currency to the home currency |
| Grand Total | `Grand_Total` | number | 0 | Total amount for the product after deducting tax and discounts |
| Sales Order Number | `SO_Number` | string |  | ID of the sales order after creating a case |
| Sales Commission | `Sales_Commission` | number | 0 | Commission of sales person on deal closure as a percentage. For example, enter 12 for 12%. |
| Status Name or ID | `Status` | options | [] | Status of the sales order. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Sub Total | `Sub_Total` | number | 0 | Total amount for the product excluding tax |
| Tax | `Tax` | number | 0 | Tax amount as the sum of sales tax and value-added tax |
| Terms and Conditions | `Terms_and_Conditions` | string |  | Terms and conditions associated with the purchase order |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Vendor ID | `vendorId` | string |  | ✓ | ID of the vendor to delete |  |
| Account ID | `accountId` | string |  | ✓ | ID of the account to delete. Can be found at the end of the URL. |  |
| Contact ID | `contactId` | string |  | ✓ | ID of the contact to delete |  |
| Deal ID | `dealId` | string |  | ✓ | ID of the deal to delete |  |
| Invoice ID | `invoiceId` | string |  | ✓ | ID of the invoice to delete |  |
| Lead ID | `leadId` | string |  | ✓ | ID of the lead to delete |  |
| Product ID | `productId` | string |  | ✓ | ID of the product to delete |  |
| Purchase Order ID | `purchaseOrderId` | string |  | ✓ | ID of the purchase order to delete |  |
| Quote ID | `quoteId` | string |  | ✓ | ID of the quote to delete |  |
| Sales Order ID | `salesOrderId` | string |  | ✓ | ID of the sales order to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Vendor ID | `vendorId` | string |  | ✓ | ID of the vendor to retrieve |  |
| Account ID | `accountId` | string |  | ✓ | ID of the account to retrieve. Can be found at the end of the URL. |  |
| Contact ID | `contactId` | string |  | ✓ | ID of the contact to retrieve |  |
| Deal ID | `dealId` | string |  | ✓ | ID of the deal to retrieve |  |
| Invoice ID | `invoiceId` | string |  | ✓ | ID of the invoice to retrieve |  |
| Lead ID | `leadId` | string |  | ✓ | ID of the lead to retrieve |  |
| Product ID | `productId` | string |  | ✓ | ID of the product to retrieve |  |
| Purchase Order ID | `purchaseOrderId` | string |  | ✓ | ID of the purchase order to retrieve |  |
| Quote ID | `quoteId` | string |  | ✓ | ID of the quote to retrieve |  |
| Sales Order ID | `salesOrderId` | string |  | ✓ | ID of the sales order to retrieve |  |

### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Vendor ID | `vendorId` | string |  | ✓ | ID of the vendor to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Category | `Category` | string |  |  |
| Currency | `Currency` | string |  |  |
| Description | `Description` | string |  |  |
| Email | `Email` | string |  |  |
| Phone | `Phone` | string |  |  |
| Vendor Name | `Vendor_Name` | string |  |  |
| Website | `Website` | string |  |  |

</details>

| Account ID | `accountId` | string |  | ✓ | ID of the account to update. Can be found at the end of the URL. |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Name of the account’s location, e.g. Headquarters or London | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Name | `Account_Name` | string |  |  |
| Account Number | `Account_Number` | string |  |  |
| Account Site | `Account_Site` | string |  | Name of the account’s location, e.g. Headquarters or London |
| Account Type Name or ID | `Account_Type` | options | [] | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Annual Revenue | `Annual_Revenue` | number |  |  |
| Contact Details | `Contact_Details` | string |  |  |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Description | `Description` | string |  |  |
| Employees | `Employees` | number |  | Number of employees in the account’s company |
| Exchange Rate | `Exchange_Rate` | number |  | Exchange rate of the default currency to the home currency |
| Fax | `Fax` | string |  |  |
| Industry | `Industry` | string |  |  |
| Phone | `Phone` | string |  |  |
| Ticker Symbol | `Ticker_Symbol` | string |  |  |
| Website | `Website` | string |  |  |

</details>

| Contact ID | `contactId` | string |  | ✓ | ID of the contact to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Phone number of the contact’s assistant | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Assistant | `Assistant` | string |  |  |
| Assistant’s Phone | `Asst_Phone` | string |  | Phone number of the contact’s assistant |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Date of Birth | `Date_of_Birth` | dateTime |  |  |
| Department | `Department` | string |  |  |
| Description | `Description` | string |  |  |
| Email (Primary) | `Email` | string |  |  |
| Email (Secondary) | `Secondary_Email` | string |  |  |
| Fax | `Fax` | string |  |  |
| First Name | `First_Name` | string |  |  |
| Full Name | `Full_Name` | string |  |  |
| Home Phone | `Home_Phone` | string |  |  |
| Last Name | `Last_Name` | string |  |  |
| Mobile | `Mobile` | string |  |  |
| Other Phone | `Other_Phone` | string |  |  |
| Phone | `Phone` | string |  |  |
| Salutation | `Salutation` | string |  |  |
| Skype ID | `Skype_ID` | string |  |  |
| Title | `Title` | string |  | Position of the contact at their company |
| Twitter | `Twitter` | string |  |  |

</details>

| Deal ID | `dealId` | string |  | ✓ | ID of the deal to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Monetary amount of the deal | e.g. Add Field | min:0, max:100 |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Amount | `Amount` | number |  | Monetary amount of the deal |
| Closing Date | `Closing_Date` | dateTime |  |  |
| Currency | `Currency` | string |  | Symbol of the currency in which revenue is generated |
| Deal Name | `Deal_Name` | string |  |  |
| Description | `Description` | string |  |  |
| Lead Conversion Time | `Lead_Conversion_Time` | number |  | Average number of days to convert the lead into a deal |
| Next Step | `Next_Step` | string |  | Description of the next step in the sales process |
| Overall Sales Duration | `Overall_Sales_Duration` | number |  | Average number of days to convert the lead into a deal and to win the deal |
| Probability | `Probability` | number |  | Probability of deal closure as a percentage. For example, enter 12 for 12%. |
| Sales Cycle Duration | `Sales_Cycle_Duration` | number | 0 | Average number of days to win the deal |
| Stage Name or ID | `Stage` | options | [] | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Invoice ID | `invoiceId` | string |  | ✓ | ID of the invoice to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the account associated with this invoice. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Name or ID | `accountId` | options | [] | ID of the account associated with this invoice. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Adjustment | `Adjustment` | number |  | Adjustment in the grand total, if any |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Description | `Description` | string |  |  |
| Due Date | `Due_Date` | dateTime |  |  |
| Exchange Rate | `Exchange_Rate` | number |  | Exchange rate of the default currency to the home currency |
| Grand Total | `Grand_Total` | number |  | Total amount for the product after deducting tax and discounts |
| Invoice Date | `Invoice_Date` | dateTime |  |  |
| Invoice Number | `Invoice_Number` | string |  |  |
| Products | `Product_Details` | collection | {} |  |
| Sales Commission | `Sales_Commission` | number |  | Commission of sales person on deal closure as a percentage. For example, enter 12 for 12%. |
| Status | `Status` | string |  |  |
| Sub Total | `Sub_Total` | number |  | Total amount for the product excluding tax |
| Subject | `Subject` | string |  | Subject or title of the invoice |
| Tax | `Tax` | number |  | Tax amount as the sum of sales tax and value-added tax |
| Terms and Conditions | `Terms_and_Conditions` | string |  | Terms and conditions associated with the invoice |

</details>

| Lead ID | `leadId` | string |  | ✓ | ID of the lead to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Annual revenue of the lead’s company | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Annual Revenue | `Annual_Revenue` | number |  | Annual revenue of the lead’s company |
| Company | `Company` | string |  | Company at which the lead works |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Description | `Description` | string |  |  |
| Designation | `Designation` | string |  | Position of the lead at their company |
| Email | `Email` | string |  |  |
| Email Opt Out | `Email_Opt_Out` | boolean | False |  |
| Fax | `Fax` | string |  |  |
| First Name | `First_Name` | string |  |  |
| Full Name | `Full_Name` | string |  |  |
| Industry | `Industry` | string |  | Industry to which the lead belongs |
| Industry Type | `Industry_Type` | string |  | Type of industry to which the lead belongs |
| Last Name | `Last_Name` | string |  |  |
| Lead Source | `Lead_Source` | string |  | Source from which the lead was created |
| Lead Status | `Lead_Status` | string |  |  |
| Mobile | `Mobile` | string |  |  |
| Number of Employees | `No_of_Employees` | number |  | Number of employees in the lead’s company |
| Phone | `Phone` | string |  |  |
| Salutation | `Salutation` | string |  |  |
| Secondary Email | `Secondary_Email` | string |  |  |
| Skype ID | `Skype_ID` | string |  |  |
| Twitter | `Twitter` | string |  |  |
| Website | `Website` | string |  |  |

</details>

| Product ID | `productId` | string |  | ✓ | ID of the product to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Commission rate for the product. For example, enter 12 for 12%. | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Commission Rate | `Commission_Rate` | number | 0 | Commission rate for the product. For example, enter 12 for 12%. |
| Description | `Description` | string |  |  |
| Manufacturer | `Manufacturer` | string |  |  |
| Product Active | `Product_Active` | boolean | False |  |
| Product Category | `Product_Category` | string |  |  |
| Quantity in Demand | `Qty_in_Demand` | number | 0 |  |
| Quantity in Stock | `Qty_in_Stock` | number | 0 |  |
| Taxable | `Taxable` | boolean | False |  |
| Unit Price | `Unit_Price` | number | 0 |  |

</details>

| Purchase Order ID | `purchaseOrderId` | string |  | ✓ | ID of the purchase order to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Adjustment in the grand total, if any | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Adjustment | `Adjustment` | number | 0 | Adjustment in the grand total, if any |
| Carrier | `Carrier` | string |  | Name of the carrier |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Description | `Description` | string |  |  |
| Discount | `Discount` | number | 0 |  |
| Due Date | `Due_Date` | dateTime |  |  |
| Exchange Rate | `Exchange_Rate` | number | 0 | Exchange rate of the default currency to the home currency |
| Grand Total | `Grand_Total` | number | 0 | Total amount for the product after deducting tax and discounts |
| PO Date | `PO_Date` | dateTime |  | Date on which the purchase order was issued |
| PO Number | `PO_Number` | string |  | ID of the purchase order after creating a case |
| Sales Commission | `Sales_Commission` | number | 0 | Commission of sales person on deal closure as a percentage. For example, enter 12 for 12%. |
| Status Name or ID | `Status` | options | [] | Status of the purchase order. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Sub Total | `Sub_Total` | number | 0 | Total amount for the product excluding tax |
| Subject | `Subject` | string |  | Subject or title of the purchase order |
| Tax | `Tax` | number | 0 | Tax amount as the sum of sales tax and value-added tax |
| Terms and Conditions | `Terms_and_Conditions` | string |  | Terms and conditions associated with the purchase order |
| Tracking Number | `Tracking_Number` | string |  |  |

</details>

| Quote ID | `quoteId` | string |  | ✓ | ID of the quote to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | Adjustment in the grand total, if any | e.g. Add Field | min:0, max:∞ |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Adjustment | `Adjustment` | number | 0 | Adjustment in the grand total, if any |
| Carrier | `Carrier` | string |  |  |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Description | `Description` | string |  |  |
| Exchange Rate | `Exchange_Rate` | number | 0 | Exchange rate of the default currency to the home currency |
| Grand Total | `Grand_Total` | number | 0 | Total amount for the product after deducting tax and discounts |
| Quote Stage Name or ID | `Quote_Stage` | options | [] | Stage of the quote. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Sub Total | `Sub_Total` | number | 0 | Total amount for the product excluding tax |
| Subject | `Subject` | string |  | Subject or title of the quote |
| Tax | `Tax` | number | 0 | Tax amount as the sum of sales tax and value-added tax |
| Team | `Team` | string |  | Team for whom the quote is created |
| Terms and Conditions | `Terms_and_Conditions` | string |  | Terms and conditions associated with the quote |
| Valid Till | `Valid_Till` | dateTime |  | Date until when the quote is valid |

</details>

| Sales Order ID | `salesOrderId` | string |  | ✓ | ID of the sales order to update |  |
| Update Fields | `updateFields` | collection | {} | ✗ | ID of the account associated with this invoice. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Name or ID | `accountId` | options | [] | ID of the account associated with this invoice. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Adjustment | `Adjustment` | number | 0 | Adjustment in the grand total, if any |
| Carrier | `Carrier` | string |  | Name of the carrier |
| Contact Name or ID | `contactId` | options | [] | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Currency | `Currency` | options | USD | Symbol of the currency in which revenue is generated |
| Deal Name or ID | `dealId` | options | [] | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Description | `Description` | string |  |  |
| Discount | `Discount` | number | 0 |  |
| Due Date | `Due_Date` | dateTime |  |  |
| Exchange Rate | `Exchange_Rate` | number | 0 | Exchange rate of the default currency to the home currency |
| Grand Total | `Grand_Total` | number | 0 | Total amount for the product after deducting tax and discounts |
| Sales Order Number | `SO_Number` | string |  | ID of the sales order after creating a case |
| Sales Commission | `Sales_Commission` | number | 0 | Commission of sales person on deal closure as a percentage. For example, enter 12 for 12%. |
| Status Name or ID | `Status` | options | [] | Status of the sales order. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Sub Total | `Sub_Total` | number | 0 | Total amount for the product excluding tax |
| Subject | `Subject` | string |  | Subject or title of the sales order |
| Tax | `Tax` | number | 0 | Tax amount as the sum of sales tax and value-added tax |
| Terms and Conditions | `Terms_and_Conditions` | string |  | Terms and conditions associated with the purchase order |

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
* Categories: Communication, Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: zohoCrm
displayName: Zoho CRM
description: Consume Zoho CRM API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: zohoOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a vendor
  params:
  - id: vendorName
    name: Vendor Name
    type: string
    default: ''
    required: true
    description: ''
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - vendor
          operation:
          - upsert
    typeInfo: &id006
      type: string
      displayName: Vendor Name
      name: vendorName
  - id: accountName
    name: Account Name
    type: string
    default: ''
    required: true
    description: ''
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - account
          operation:
          - upsert
    typeInfo: &id008
      type: string
      displayName: Account Name
      name: accountName
  - id: lastName
    name: Last Name
    type: string
    default: ''
    required: true
    description: ''
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - lead
          operation:
          - upsert
    typeInfo: &id002
      type: string
      displayName: Last Name
      name: lastName
  - id: dealName
    name: Deal Name
    type: string
    default: ''
    required: true
    description: ''
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - upsert
    typeInfo: &id010
      type: string
      displayName: Deal Name
      name: dealName
  - id: stage
    name: Stage Name or ID
    type: options
    default: &id011 []
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id012
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - create
          - upsert
    typeInfo: &id013
      type: options
      displayName: Stage Name or ID
      name: stage
      typeOptions:
        loadOptionsMethod: getDealStage
      possibleValues: []
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: Subject or title of the invoice
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - salesOrder
          operation:
          - upsert
    typeInfo: &id004
      type: string
      displayName: Subject
      name: subject
  - id: Company
    name: Company
    type: string
    default: ''
    required: true
    description: Company at which the lead works
    validation: &id014
      required: true
      displayOptions:
        show:
          resource:
          - lead
          operation:
          - upsert
    typeInfo: &id015
      type: string
      displayName: Company
      name: Company
  - id: lastName
    name: Last Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: productName
    name: Product Name
    type: string
    default: ''
    required: true
    description: ''
    validation: &id016
      required: true
      displayOptions:
        show:
          resource:
          - product
          operation:
          - upsert
    typeInfo: &id017
      type: string
      displayName: Product Name
      name: productName
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: Subject or title of the purchase order
    validation: *id003
    typeInfo: *id004
  - id: vendorId
    name: Vendor Name or ID
    type: options
    default: &id018 []
    required: false
    description: ID of the vendor associated with the purchase order. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id019
      displayOptions:
        show:
          resource:
          - purchaseOrder
          operation:
          - create
          - upsert
    typeInfo: &id020
      type: options
      displayName: Vendor Name or ID
      name: vendorId
      typeOptions:
        loadOptionsMethod: getVendors
      possibleValues: []
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: Subject or title of the quote
    validation: *id003
    typeInfo: *id004
  - id: accountId
    name: Account Name or ID
    type: options
    default: &id021 []
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id022
      required: true
      displayOptions:
        show:
          resource:
          - salesOrder
          operation:
          - create
          - upsert
    typeInfo: &id023
      type: options
      displayName: Account Name or ID
      name: accountId
      typeOptions:
        loadOptionsMethod: getAccounts
      possibleValues: []
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: Subject or title of the sales order
    validation: *id003
    typeInfo: *id004
- id: upsert
  name: Create or Update
  description: Create a new record, or update the current one if it already exists
    (upsert)
  params:
  - id: vendorName
    name: Vendor Name
    type: string
    default: ''
    required: true
    description: Name of the vendor. If a record with this vendor name exists it will
      be updated, otherwise a new one will be created.
    validation: *id005
    typeInfo: *id006
  - id: accountName
    name: Account Name
    type: string
    default: ''
    required: true
    description: Name of the account. If a record with this account name exists it
      will be updated, otherwise a new one will be created.
    validation: *id007
    typeInfo: *id008
  - id: lastName
    name: Last Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: dealName
    name: Deal Name
    type: string
    default: ''
    required: true
    description: Name of the deal. If a record with this deal name exists it will
      be updated, otherwise a new one will be created.
    validation: *id009
    typeInfo: *id010
  - id: stage
    name: Stage Name or ID
    type: options
    default: *id011
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id012
    typeInfo: *id013
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: Subject or title of the invoice. If a record with this subject exists
      it will be updated, otherwise a new one will be created.
    validation: *id003
    typeInfo: *id004
  - id: Company
    name: Company
    type: string
    default: ''
    required: true
    description: Company at which the lead works
    validation: *id014
    typeInfo: *id015
  - id: lastName
    name: Last Name
    type: string
    default: ''
    required: true
    description: ''
    validation: *id001
    typeInfo: *id002
  - id: productName
    name: Product Name
    type: string
    default: ''
    required: true
    description: Name of the product. If a record with this product name exists it
      will be updated, otherwise a new one will be created.
    validation: *id016
    typeInfo: *id017
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: Subject or title of the purchase order. If a record with this subject
      exists it will be updated, otherwise a new one will be created.
    validation: *id003
    typeInfo: *id004
  - id: vendorId
    name: Vendor Name or ID
    type: options
    default: *id018
    required: false
    description: ID of the vendor associated with the purchase order. Choose from
      the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id019
    typeInfo: *id020
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: Subject or title of the quote. If a record with this subject exists
      it will be updated, otherwise a new one will be created.
    validation: *id003
    typeInfo: *id004
  - id: accountId
    name: Account Name or ID
    type: options
    default: *id021
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id022
    typeInfo: *id023
  - id: subject
    name: Subject
    type: string
    default: ''
    required: true
    description: Subject or title of the sales order. If a record with this subject
      exists it will be updated, otherwise a new one will be created.
    validation: *id003
    typeInfo: *id004
- id: delete
  name: Delete
  description: Delete a vendor
  params:
  - id: vendorId
    name: Vendor ID
    type: string
    default: ''
    required: true
    description: ID of the vendor to delete
    validation: *id019
    typeInfo: *id020
  - id: accountId
    name: Account ID
    type: string
    default: ''
    required: true
    description: ID of the account to delete. Can be found at the end of the URL.
    validation: *id022
    typeInfo: *id023
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact to delete
    validation: &id024
      required: true
      displayOptions:
        show:
          resource:
          - contact
          operation:
          - update
    typeInfo: &id025
      type: string
      displayName: Contact ID
      name: contactId
  - id: dealId
    name: Deal ID
    type: string
    default: ''
    required: true
    description: ID of the deal to delete
    validation: &id026
      required: true
      displayOptions:
        show:
          resource:
          - deal
          operation:
          - update
    typeInfo: &id027
      type: string
      displayName: Deal ID
      name: dealId
  - id: invoiceId
    name: Invoice ID
    type: string
    default: ''
    required: true
    description: ID of the invoice to delete
    validation: &id028
      required: true
      displayOptions:
        show:
          resource:
          - invoice
          operation:
          - update
    typeInfo: &id029
      type: string
      displayName: Invoice ID
      name: invoiceId
  - id: leadId
    name: Lead ID
    type: string
    default: ''
    required: true
    description: ID of the lead to delete
    validation: &id030
      required: true
      displayOptions:
        show:
          resource:
          - lead
          operation:
          - update
    typeInfo: &id031
      type: string
      displayName: Lead ID
      name: leadId
  - id: productId
    name: Product ID
    type: string
    default: ''
    required: true
    description: ID of the product to delete
    validation: &id032
      required: true
      displayOptions:
        show:
          resource:
          - product
          operation:
          - update
    typeInfo: &id033
      type: string
      displayName: Product ID
      name: productId
  - id: purchaseOrderId
    name: Purchase Order ID
    type: string
    default: ''
    required: true
    description: ID of the purchase order to delete
    validation: &id034
      required: true
      displayOptions:
        show:
          resource:
          - purchaseOrder
          operation:
          - update
    typeInfo: &id035
      type: string
      displayName: Purchase Order ID
      name: purchaseOrderId
  - id: quoteId
    name: Quote ID
    type: string
    default: ''
    required: true
    description: ID of the quote to delete
    validation: &id036
      required: true
      displayOptions:
        show:
          resource:
          - quote
          operation:
          - update
    typeInfo: &id037
      type: string
      displayName: Quote ID
      name: quoteId
  - id: salesOrderId
    name: Sales Order ID
    type: string
    default: ''
    required: true
    description: ID of the sales order to delete
    validation: &id038
      required: true
      displayOptions:
        show:
          resource:
          - salesOrder
          operation:
          - update
    typeInfo: &id039
      type: string
      displayName: Sales Order ID
      name: salesOrderId
- id: get
  name: Get
  description: Get a vendor
  params:
  - id: vendorId
    name: Vendor ID
    type: string
    default: ''
    required: true
    description: ID of the vendor to retrieve
    validation: *id019
    typeInfo: *id020
  - id: accountId
    name: Account ID
    type: string
    default: ''
    required: true
    description: ID of the account to retrieve. Can be found at the end of the URL.
    validation: *id022
    typeInfo: *id023
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact to retrieve
    validation: *id024
    typeInfo: *id025
  - id: dealId
    name: Deal ID
    type: string
    default: ''
    required: true
    description: ID of the deal to retrieve
    validation: *id026
    typeInfo: *id027
  - id: invoiceId
    name: Invoice ID
    type: string
    default: ''
    required: true
    description: ID of the invoice to retrieve
    validation: *id028
    typeInfo: *id029
  - id: leadId
    name: Lead ID
    type: string
    default: ''
    required: true
    description: ID of the lead to retrieve
    validation: *id030
    typeInfo: *id031
  - id: productId
    name: Product ID
    type: string
    default: ''
    required: true
    description: ID of the product to retrieve
    validation: *id032
    typeInfo: *id033
  - id: purchaseOrderId
    name: Purchase Order ID
    type: string
    default: ''
    required: true
    description: ID of the purchase order to retrieve
    validation: *id034
    typeInfo: *id035
  - id: quoteId
    name: Quote ID
    type: string
    default: ''
    required: true
    description: ID of the quote to retrieve
    validation: *id036
    typeInfo: *id037
  - id: salesOrderId
    name: Sales Order ID
    type: string
    default: ''
    required: true
    description: ID of the sales order to retrieve
    validation: *id038
    typeInfo: *id039
- id: getAll
  name: Get Many
  description: Get many vendors
- id: update
  name: Update
  description: Update a vendor
  params:
  - id: vendorId
    name: Vendor ID
    type: string
    default: ''
    required: true
    description: ID of the vendor to update
    validation: *id019
    typeInfo: *id020
  - id: accountId
    name: Account ID
    type: string
    default: ''
    required: true
    description: ID of the account to update. Can be found at the end of the URL.
    validation: *id022
    typeInfo: *id023
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ID of the contact to update
    validation: *id024
    typeInfo: *id025
  - id: dealId
    name: Deal ID
    type: string
    default: ''
    required: true
    description: ID of the deal to update
    validation: *id026
    typeInfo: *id027
  - id: invoiceId
    name: Invoice ID
    type: string
    default: ''
    required: true
    description: ID of the invoice to update
    validation: *id028
    typeInfo: *id029
  - id: leadId
    name: Lead ID
    type: string
    default: ''
    required: true
    description: ID of the lead to update
    validation: *id030
    typeInfo: *id031
  - id: productId
    name: Product ID
    type: string
    default: ''
    required: true
    description: ID of the product to update
    validation: *id032
    typeInfo: *id033
  - id: purchaseOrderId
    name: Purchase Order ID
    type: string
    default: ''
    required: true
    description: ID of the purchase order to update
    validation: *id034
    typeInfo: *id035
  - id: quoteId
    name: Quote ID
    type: string
    default: ''
    required: true
    description: ID of the quote to update
    validation: *id036
    typeInfo: *id037
  - id: salesOrderId
    name: Sales Order ID
    type: string
    default: ''
    required: true
    description: ID of the sales order to update
    validation: *id038
    typeInfo: *id039
- id: getFields
  name: Get Fields
  description: Get lead fields
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
  - field: Product_Details
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
  - field: Product_Details
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: Product_Details
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: Product_Details
    text: Add Field
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
  "$id": "https://n8n.io/schemas/nodes/zohoCrm.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Zoho CRM Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "upsert",
        "delete",
        "get",
        "getAll",
        "update",
        "getFields"
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
            "contact",
            "deal",
            "invoice",
            "lead",
            "product",
            "purchaseOrder",
            "quote",
            "salesOrder",
            "vendor"
          ],
          "default": "account"
        },
        "operation": {
          "description": "Create a sales order",
          "type": "string",
          "enum": [
            "create",
            "upsert",
            "delete",
            "get",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "vendorName": {
          "description": "Name of the vendor. If a record with this vendor name exists it will be updated, otherwise a new one will be created.",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Adjustment in the grand total, if any",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "vendorId": {
          "description": "ID of the vendor associated with the purchase order. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "updateFields": {
          "description": "ID of the account associated with this invoice. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "accountName": {
          "description": "Name of the account. If a record with this account name exists it will be updated, otherwise a new one will be created.",
          "type": "string",
          "default": ""
        },
        "accountId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": []
        },
        "lastName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "contactId": {
          "description": "ID of the contact to update",
          "type": "string",
          "default": ""
        },
        "dealName": {
          "description": "Name of the deal. If a record with this deal name exists it will be updated, otherwise a new one will be created.",
          "type": "string",
          "default": ""
        },
        "stage": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": []
        },
        "dealId": {
          "description": "ID of the deal to update",
          "type": "string",
          "default": ""
        },
        "subject": {
          "description": "Subject or title of the sales order. If a record with this subject exists it will be updated, otherwise a new one will be created.",
          "type": "string",
          "default": ""
        },
        "Product_Details": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "invoiceId": {
          "description": "ID of the invoice to update",
          "type": "string",
          "default": ""
        },
        "Company": {
          "description": "Company at which the lead works",
          "type": "string",
          "default": ""
        },
        "leadId": {
          "description": "ID of the lead to update",
          "type": "string",
          "default": ""
        },
        "productName": {
          "description": "Name of the product. If a record with this product name exists it will be updated, otherwise a new one will be created.",
          "type": "string",
          "default": ""
        },
        "productId": {
          "description": "ID of the product to update",
          "type": "string",
          "default": ""
        },
        "purchaseOrderId": {
          "description": "ID of the purchase order to update",
          "type": "string",
          "default": ""
        },
        "quoteId": {
          "description": "ID of the quote to update",
          "type": "string",
          "default": ""
        },
        "salesOrderId": {
          "description": "ID of the sales order to update",
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
      "name": "zohoOAuth2Api",
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
