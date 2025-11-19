---
title: "Node: QuickBooks Online"
slug: "node-quickbooks"
version: "1"
updated: "2025-11-13"
summary: "Consume the QuickBooks Online API"
node_type: "regular"
group: "['transform']"
---

# Node: QuickBooks Online

**Purpose.** Consume the QuickBooks Online API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:quickbooks.svg`
- **Group:** `['transform']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **quickBooksOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `quickBooksOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** user-agent

---

## Operations

### Transaction Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get Report | `getReport` | Get a report |

### Bill Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a bill |
| Delete | `delete` | Delete a bill |
| Get | `get` | Get a bill |
| Get Many | `getAll` | Get many bills |
| Update | `update` | Update a bill |

### Customer Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a customer |
| Get | `get` | Get a customer |
| Get Many | `getAll` | Get many customers |
| Update | `update` | Update a customer |

### Employee Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an employee |
| Get | `get` | Get an employee |
| Get Many | `getAll` | Get many employees |
| Update | `update` | Update an employee |

### Estimate Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an estimate |
| Delete | `delete` | Delete an estimate |
| Get | `get` | Get an estimate |
| Get Many | `getAll` | Get many estimates |
| Send | `send` | Send an estimate |
| Update | `update` | Update an estimate |

### Invoice Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create an invoice |
| Delete | `delete` | Delete an invoice |
| Get | `get` | Get an invoice |
| Get Many | `getAll` | Get many invoices |
| Send | `send` | Send an invoice |
| Update | `update` | Update an invoice |
| Void | `void` | Void an invoice |

### Item Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get an item |
| Get Many | `getAll` | Get many items |

### Payment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a payment |
| Delete | `delete` | Delete a payment |
| Get | `get` | Get a payment |
| Get Many | `getAll` | Get many payments |
| Send | `send` | Send a payment |
| Update | `update` | Update a payment |
| Void | `void` | Void a payment |

### Vendor Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a vendor |
| Get | `get` | Get a vendor |
| Get Many | `getAll` | Get many vendors |
| Update | `update` | Update a vendor |

### Purchase Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Get | `get` | Get a purchase |
| Get Many | `getAll` | Get many purchases |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | customer | ✗ | Resource to operate on |  |

**Resource options:**

* **Bill** (`bill`)
* **Customer** (`customer`)
* **Employee** (`employee`)
* **Estimate** (`estimate`)
* **Invoice** (`invoice`)
* **Item** (`item`)
* **Payment** (`payment`)
* **Purchase** (`purchase`)
* **Transaction** (`transaction`)
* **Vendor** (`vendor`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | getReport | ✗ | Operation to perform |  |

**Operation options:**

* **Get Report** (`getReport`) - Get a report

---

### Get Report parameters (`getReport`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Simplify | `simple` | boolean | True | ✗ | Whether to return a simplified version of the response instead of the raw data |  |
| Filters | `filters` | collection | {} | ✗ | Columns to return | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Accounts Payable Paid | `appaid` | options | All |  |
| Accounts Receivable Paid | `arpaid` | options | All |  |
| Cleared Status | `cleared` | options | Reconciled |  |
| Columns | `columns` | multiOptions | [] | Columns to return |
| Customer Names or IDs | `customer` | multiOptions | [] | Customer to filter results by. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Date Range (Custom) | `dateRangeCustom` | fixedCollection | {} | Start date of the date range to filter results by |
| Date Range (Predefined) | `date_macro` | options | This Month | Predefined date range to filter results by |
| Date Range for Creation Date (Custom) | `dateRangeCreationCustom` | fixedCollection | {} | Start date of the account creation date range to filter results by |
| Date Range for Creation Date (Predefined) | `createdate_macro` | options | This Month | Predefined report account creation date range |
| Date Range for Due Date (Custom) | `dateRangeDueCustom` | fixedCollection | {} | Start date of the due date range to filter results by |
| Date Range for Due Date (Predefined) | `duedate_macro` | options | This Month | Predefined due date range to filter results by |
| Date Range for Modification Date (Custom) | `dateRangeModificationCustom` | fixedCollection | {} | Start date of the account modification date range to filter results by |
| Date Range for Modification Date (Predefined) | `moddate_macro` | options | This Month | Predefined account modifiction date range to filter results by |
| Department Names or IDs | `department` | multiOptions | [] | Department to filter results by. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Document Number | `docnum` | string |  | Transaction document number to filter results by |
| Group By | `group_by` | options | Account | Transaction field to group results by |
| Memo Names or IDs | `memo` | multiOptions | [] | Memo to filter results by. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Payment Method | `payment_Method` | options | Cash | Payment method to filter results by |
| Printed Status | `printed` | options | Printed | Printed state to filter results by |
| Quick Zoom URL | `qzurl` | boolean | True | Whether Quick Zoom URL information should be generated |
| Sort By | `sort_by` | options | account_name | Column to sort results by |
| Sort Order | `sort_order` | options | Ascend |  |
| Source Account Type | `source_account_type` | options | Bank | Account type to filter results by |
| Term Names or IDs | `term` | multiOptions | [] | Term to filter results by. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Transaction Amount | `bothamount` | number | 0 | Monetary amount to filter results by |
| Transaction Type | `transaction_type` | options | CreditCardCharge | Transaction type to filter results by |
| Vendor Names or IDs | `vendor` | multiOptions | [] | Vendor to filter results by. Choose from the list, or specify IDs using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |

</details>


### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| For Vendor Name or ID | `VendorRef` | options | [] | ✓ | The ID of the vendor who the bill is for. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Line | `Line` | collection | {} | ✗ | Individual line item of a transaction | e.g. Add Line Item Property |  |

<details>
<summary><strong>Line sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account ID | `accountId` | string |  |  |
| Amount | `Amount` | number | 0 | Monetary amount of the line item |
| Description | `Description` | string |  | Textual description of the line item |
| Detail Type | `DetailType` | options | ItemBasedExpenseLineDetail |  |
| Item Name or ID | `itemId` | options | [] | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Position | `LineNum` | number | 1 | Position of the line item relative to others |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| Display Name | `displayName` | string |  | ✓ | The display name of the customer to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| Family Name | `FamilyName` | string |  | ✗ |  |  |
| Given Name | `GivenName` | string |  | ✗ |  |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| For Customer Name or ID | `CustomerRef` | options | [] | ✓ | The ID of the customer who the estimate is for. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Line | `Line` | collection | {} | ✗ | Individual line item of a transaction | e.g. Add Line Item Property |  |

<details>
<summary><strong>Line sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Amount | `Amount` | number | 0 | Monetary amount of the line item |
| Description | `Description` | string |  | Textual description of the line item |
| Detail Type | `DetailType` | options | SalesItemLineDetail |  |
| Item Name or ID | `itemId` | options | [] | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Position | `LineNum` | number | 1 | Position of the line item relative to others |
| Tax Code Ref Name or ID | `TaxCodeRef` | options | [] | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| For Customer Name or ID | `CustomerRef` | options | [] | ✓ | The ID of the customer who the invoice is for. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Line | `Line` | collection | {} | ✗ | Individual line item of a transaction | e.g. Add Line Item Property |  |

<details>
<summary><strong>Line sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Amount | `Amount` | number | 0 | Monetary amount of the line item |
| Description | `Description` | string |  | Textual description of the line item |
| Detail Type | `DetailType` | options | SalesItemLineDetail |  |
| Item Name or ID | `itemId` | options | [] | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Position | `LineNum` | number | 1 | Position of the line item relative to others |
| Tax Code Ref Name or ID | `TaxCodeRef` | options | [] | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Quantity | `Qty` | number | 0 | Number of units of the line item |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| For Customer Name or ID | `CustomerRef` | options | [] | ✓ | The ID of the customer who the payment is for. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |  |
| Total Amount | `TotalAmt` | number | 0 | ✗ | Total amount of the transaction |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |
| Display Name | `displayName` | string |  | ✓ | The display name of the vendor to create |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Bill ID | `billId` | string |  | ✓ | The ID of the bill to delete |  |
| Estimate ID | `estimateId` | string |  | ✓ | The ID of the estimate to delete |  |
| Invoice ID | `invoiceId` | string |  | ✓ | The ID of the invoice to delete |  |
| Payment ID | `paymentId` | string |  | ✓ | The ID of the payment to delete |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Bill ID | `billId` | string |  | ✓ | The ID of the bill to retrieve |  |
| Customer ID | `customerId` | string |  | ✓ | The ID of the customer to retrieve |  |
| Employee ID | `employeeId` | string |  | ✓ | The ID of the employee to retrieve |  |
| Estimate ID | `estimateId` | string |  | ✓ | The ID of the estimate to retrieve |  |
| Download | `download` | boolean | False | ✓ | Whether to download the estimate as a PDF file |  |
| Put Output File in Field | `binaryProperty` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |
| File Name | `fileName` | string |  | ✓ | Name of the file that will be downloaded | e.g. data.pdf |  |
| Invoice ID | `invoiceId` | string |  | ✓ | The ID of the invoice to retrieve |  |
| Download | `download` | boolean | False | ✓ | Whether to download the invoice as a PDF file |  |
| Put Output File in Field | `binaryProperty` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |
| File Name | `fileName` | string |  | ✓ | Name of the file that will be downloaded | e.g. data.pdf |  |
| Item ID | `itemId` | string |  | ✓ | The ID of the item to retrieve |  |
| Payment ID | `paymentId` | string |  | ✓ | The ID of the payment to retrieve |  |
| Download | `download` | boolean | False | ✓ | Whether to download estimate as PDF file |  |
| Put Output File in Field | `binaryProperty` | string | data | ✓ | e.g. The name of the output binary field to put the file in |  |
| File Name | `fileName` | string |  | ✓ | Name of the file that will be downloaded | e.g. data.pdf |  |
| Vendor ID | `vendorId` | string |  | ✓ | The ID of the vendor to retrieve |  |
| Purchase ID | `purchaseId` | string |  | ✓ | The ID of the purchase to retrieve |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | The condition for selecting bills. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` | string |  | The condition for selecting bills. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | The condition for selecting customers. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` | string |  | The condition for selecting customers. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | The condition for selecting employees. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` | string |  | The condition for selecting employees. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | The condition for selecting estimates. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` | string |  | The condition for selecting estimates. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | The condition for selecting invoices. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` | string |  | The condition for selecting invoices. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | The condition for selecting items. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` | string |  | The condition for selecting items. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | The condition for selecting payments. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` | string |  | The condition for selecting payments. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | The condition for selecting vendors. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` | string |  | The condition for selecting vendors. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:1000 |
| Filters | `filters` | collection | {} | ✗ | The condition for selecting purchases. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. | e.g. Add Field |  |

<details>
<summary><strong>Filters sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Query | `query` | string |  | The condition for selecting purchases. See the <a href="https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries">guide</a> for supported syntax. |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Bill ID | `billId` | string |  | ✓ | The ID of the bill to update |  |
| Update Fields | `updateFields` | collection | {} | ✓ | e.g. Add Field |  |
| Customer ID | `customerId` | string |  | ✓ | The ID of the customer to update |  |
| Update Fields | `updateFields` | collection | {} | ✓ | e.g. Add Field |  |
| Employee ID | `employeeId` | string |  | ✓ | The ID of the employee to update |  |
| Update Fields | `updateFields` | collection | {} | ✓ | e.g. Add Field |  |
| Estimate ID | `estimateId` | string |  | ✓ | The ID of the estimate to update |  |
| Update Fields | `updateFields` | collection | {} | ✓ | e.g. Add Field |  |
| Invoice ID | `invoiceId` | string |  | ✓ | The ID of the invoice to update |  |
| Update Fields | `updateFields` | collection | {} | ✓ | e.g. Add Field |  |
| Payment ID | `paymentId` | string |  | ✓ | The ID of the payment to update |  |
| Update Fields | `updateFields` | collection | {} | ✓ | e.g. Add Field |  |
| Vendor ID | `vendorId` | string |  | ✓ | The ID of the vendor to update |  |
| Update Fields | `updateFields` | collection | {} | ✓ | e.g. Add Field |  |

### Send parameters (`send`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Estimate ID | `estimateId` | string |  | ✓ | The ID of the estimate to send |  |
| Email | `email` | string |  | ✓ | The email of the recipient of the estimate | e.g. name@email.com | email |
| Invoice ID | `invoiceId` | string |  | ✓ | The ID of the invoice to send |  |
| Email | `email` | string |  | ✓ | The email of the recipient of the invoice | e.g. name@email.com | email |
| Payment ID | `paymentId` | string |  | ✓ | The ID of the payment to send |  |
| Email | `email` | string |  | ✓ | The email of the recipient of the payment | e.g. name@email.com | email |

### Void parameters (`void`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Invoice ID | `invoiceId` | string |  | ✓ | The ID of the invoice to void |  |
| Payment ID | `paymentId` | string |  | ✓ | The ID of the payment to void |  |

---

## Load Options Methods

- `getCustomers`

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
* Categories: Finance & Accounting

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: quickbooks
displayName: QuickBooks Online
description: Consume the QuickBooks Online API
version: '1'
nodeType: regular
group:
- transform
credentials:
- name: quickBooksOAuth2Api
  required: true
operations:
- id: getReport
  name: Get Report
  description: ''
  params:
  - id: simple
    name: Simplify
    type: boolean
    default: true
    required: false
    description: Whether to return a simplified version of the response instead of
      the raw data
    validation:
      displayOptions:
        show:
          resource:
          - transaction
          operation:
          - getReport
    typeInfo:
      type: boolean
      displayName: Simplify
      name: simple
- id: create
  name: Create
  description: ''
  params:
  - id: VendorRef
    name: For Vendor Name or ID
    type: options
    default: []
    required: true
    description: The ID of the vendor who the bill is for. Choose from the list, or
      specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - bill
          operation:
          - create
    typeInfo:
      type: options
      displayName: For Vendor Name or ID
      name: VendorRef
      typeOptions:
        loadOptionsMethod: getVendors
      possibleValues: []
  - id: displayName
    name: Display Name
    type: string
    default: ''
    required: true
    description: The display name of the customer to create
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - vendor
          operation:
          - create
    typeInfo: &id004
      type: string
      displayName: Display Name
      name: displayName
  - id: FamilyName
    name: Family Name
    type: string
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - employee
          operation:
          - create
    typeInfo:
      type: string
      displayName: Family Name
      name: FamilyName
  - id: GivenName
    name: Given Name
    type: string
    default: ''
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          resource:
          - employee
          operation:
          - create
    typeInfo:
      type: string
      displayName: Given Name
      name: GivenName
  - id: CustomerRef
    name: For Customer Name or ID
    type: options
    default: []
    required: true
    description: The ID of the customer who the estimate is for. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - payment
          operation:
          - create
    typeInfo: &id002
      type: options
      displayName: For Customer Name or ID
      name: CustomerRef
      typeOptions:
        loadOptionsMethod: getCustomers
      possibleValues: []
  - id: CustomerRef
    name: For Customer Name or ID
    type: options
    default: []
    required: true
    description: The ID of the customer who the invoice is for. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: CustomerRef
    name: For Customer Name or ID
    type: options
    default: []
    required: true
    description: The ID of the customer who the payment is for. Choose from the list,
      or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>.
    validation: *id001
    typeInfo: *id002
  - id: TotalAmt
    name: Total Amount
    type: number
    default: 0
    required: false
    description: Total amount of the transaction
    validation:
      displayOptions:
        show:
          resource:
          - payment
          operation:
          - create
    typeInfo:
      type: number
      displayName: Total Amount
      name: TotalAmt
  - id: displayName
    name: Display Name
    type: string
    default: ''
    required: true
    description: The display name of the vendor to create
    validation: *id003
    typeInfo: *id004
- id: delete
  name: Delete
  description: ''
  params:
  - id: billId
    name: Bill ID
    type: string
    default: ''
    required: true
    description: The ID of the bill to delete
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - bill
          operation:
          - update
    typeInfo: &id006
      type: string
      displayName: Bill ID
      name: billId
  - id: estimateId
    name: Estimate ID
    type: string
    default: ''
    required: true
    description: The ID of the estimate to delete
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - estimate
          operation:
          - update
    typeInfo: &id008
      type: string
      displayName: Estimate ID
      name: estimateId
  - id: invoiceId
    name: Invoice ID
    type: string
    default: ''
    required: true
    description: The ID of the invoice to delete
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - invoice
          operation:
          - update
    typeInfo: &id010
      type: string
      displayName: Invoice ID
      name: invoiceId
  - id: paymentId
    name: Payment ID
    type: string
    default: ''
    required: true
    description: The ID of the payment to delete
    validation: &id017
      required: true
      displayOptions:
        show:
          resource:
          - payment
          operation:
          - update
    typeInfo: &id018
      type: string
      displayName: Payment ID
      name: paymentId
- id: get
  name: Get
  description: ''
  params:
  - id: billId
    name: Bill ID
    type: string
    default: ''
    required: true
    description: The ID of the bill to retrieve
    validation: *id005
    typeInfo: *id006
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: The ID of the customer to retrieve
    validation: &id023
      required: true
      displayOptions:
        show:
          resource:
          - customer
          operation:
          - update
    typeInfo: &id024
      type: string
      displayName: Customer ID
      name: customerId
  - id: employeeId
    name: Employee ID
    type: string
    default: ''
    required: true
    description: The ID of the employee to retrieve
    validation: &id025
      required: true
      displayOptions:
        show:
          resource:
          - employee
          operation:
          - update
    typeInfo: &id026
      type: string
      displayName: Employee ID
      name: employeeId
  - id: estimateId
    name: Estimate ID
    type: string
    default: ''
    required: true
    description: The ID of the estimate to retrieve
    validation: *id007
    typeInfo: *id008
  - id: download
    name: Download
    type: boolean
    default: false
    required: true
    description: Whether to download the estimate as a PDF file
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - payment
          operation:
          - get
    typeInfo: &id012
      type: boolean
      displayName: Download
      name: download
  - id: binaryProperty
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - payment
          operation:
          - get
          download:
          - true
    typeInfo: &id014
      type: string
      displayName: Put Output File in Field
      name: binaryProperty
  - id: fileName
    name: File Name
    type: string
    default: ''
    required: true
    description: Name of the file that will be downloaded
    placeholder: data.pdf
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - payment
          operation:
          - get
          download:
          - true
    typeInfo: &id016
      type: string
      displayName: File Name
      name: fileName
  - id: invoiceId
    name: Invoice ID
    type: string
    default: ''
    required: true
    description: The ID of the invoice to retrieve
    validation: *id009
    typeInfo: *id010
  - id: download
    name: Download
    type: boolean
    default: false
    required: true
    description: Whether to download the invoice as a PDF file
    validation: *id011
    typeInfo: *id012
  - id: binaryProperty
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: *id013
    typeInfo: *id014
  - id: fileName
    name: File Name
    type: string
    default: ''
    required: true
    description: Name of the file that will be downloaded
    placeholder: data.pdf
    validation: *id015
    typeInfo: *id016
  - id: itemId
    name: Item ID
    type: string
    default: ''
    required: true
    description: The ID of the item to retrieve
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - item
          operation:
          - get
    typeInfo:
      type: string
      displayName: Item ID
      name: itemId
  - id: paymentId
    name: Payment ID
    type: string
    default: ''
    required: true
    description: The ID of the payment to retrieve
    validation: *id017
    typeInfo: *id018
  - id: download
    name: Download
    type: boolean
    default: false
    required: true
    description: Whether to download estimate as PDF file
    validation: *id011
    typeInfo: *id012
  - id: binaryProperty
    name: Put Output File in Field
    type: string
    default: data
    required: true
    description: ''
    hint: The name of the output binary field to put the file in
    validation: *id013
    typeInfo: *id014
  - id: fileName
    name: File Name
    type: string
    default: ''
    required: true
    description: Name of the file that will be downloaded
    placeholder: data.pdf
    validation: *id015
    typeInfo: *id016
  - id: vendorId
    name: Vendor ID
    type: string
    default: ''
    required: true
    description: The ID of the vendor to retrieve
    validation: &id027
      required: true
      displayOptions:
        show:
          resource:
          - vendor
          operation:
          - update
    typeInfo: &id028
      type: string
      displayName: Vendor ID
      name: vendorId
  - id: purchaseId
    name: Purchase ID
    type: string
    default: ''
    required: true
    description: The ID of the purchase to retrieve
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - purchase
          operation:
          - get
    typeInfo:
      type: string
      displayName: Purchase ID
      name: purchaseId
- id: getAll
  name: Get Many
  description: ''
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id019
      displayOptions:
        show:
          resource:
          - purchase
          operation:
          - getAll
    typeInfo: &id020
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id021
      displayOptions:
        show:
          resource:
          - purchase
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id022
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 1000
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id019
    typeInfo: *id020
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id021
    typeInfo: *id022
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id019
    typeInfo: *id020
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id021
    typeInfo: *id022
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id019
    typeInfo: *id020
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id021
    typeInfo: *id022
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id019
    typeInfo: *id020
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id021
    typeInfo: *id022
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id019
    typeInfo: *id020
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id021
    typeInfo: *id022
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id019
    typeInfo: *id020
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id021
    typeInfo: *id022
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id019
    typeInfo: *id020
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id021
    typeInfo: *id022
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id019
    typeInfo: *id020
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id021
    typeInfo: *id022
- id: update
  name: Update
  description: ''
  params:
  - id: billId
    name: Bill ID
    type: string
    default: ''
    required: true
    description: The ID of the bill to update
    validation: *id005
    typeInfo: *id006
  - id: customerId
    name: Customer ID
    type: string
    default: ''
    required: true
    description: The ID of the customer to update
    validation: *id023
    typeInfo: *id024
  - id: employeeId
    name: Employee ID
    type: string
    default: ''
    required: true
    description: The ID of the employee to update
    validation: *id025
    typeInfo: *id026
  - id: estimateId
    name: Estimate ID
    type: string
    default: ''
    required: true
    description: The ID of the estimate to update
    validation: *id007
    typeInfo: *id008
  - id: invoiceId
    name: Invoice ID
    type: string
    default: ''
    required: true
    description: The ID of the invoice to update
    validation: *id009
    typeInfo: *id010
  - id: paymentId
    name: Payment ID
    type: string
    default: ''
    required: true
    description: The ID of the payment to update
    validation: *id017
    typeInfo: *id018
  - id: vendorId
    name: Vendor ID
    type: string
    default: ''
    required: true
    description: The ID of the vendor to update
    validation: *id027
    typeInfo: *id028
- id: send
  name: Send
  description: ''
  params:
  - id: estimateId
    name: Estimate ID
    type: string
    default: ''
    required: true
    description: The ID of the estimate to send
    validation: *id007
    typeInfo: *id008
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email of the recipient of the estimate
    placeholder: name@email.com
    validation: &id029
      required: true
      format: email
      displayOptions:
        show:
          resource:
          - payment
          operation:
          - send
    typeInfo: &id030
      type: string
      displayName: Email
      name: email
  - id: invoiceId
    name: Invoice ID
    type: string
    default: ''
    required: true
    description: The ID of the invoice to send
    validation: *id009
    typeInfo: *id010
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email of the recipient of the invoice
    placeholder: name@email.com
    validation: *id029
    typeInfo: *id030
  - id: paymentId
    name: Payment ID
    type: string
    default: ''
    required: true
    description: The ID of the payment to send
    validation: *id017
    typeInfo: *id018
  - id: email
    name: Email
    type: string
    default: ''
    required: true
    description: The email of the recipient of the payment
    placeholder: name@email.com
    validation: *id029
    typeInfo: *id030
- id: void
  name: Void
  description: ''
  params:
  - id: invoiceId
    name: Invoice ID
    type: string
    default: ''
    required: true
    description: The ID of the invoice to void
    validation: *id009
    typeInfo: *id010
  - id: paymentId
    name: Payment ID
    type: string
    default: ''
    required: true
    description: The ID of the payment to void
    validation: *id017
    typeInfo: *id018
common_expressions:
- '={{$parameter["operation"] + ": " + $parameter["resource"]}}'
api_patterns:
  http_methods: []
  endpoints: []
  headers:
  - user-agent
  query_params: []
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: filters
    text: Add Field
  - field: Line
    text: Add Line Item Property
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: Line
    text: Add Line Item Property
  - field: additionalFields
    text: Add Field
  - field: fileName
    text: data.pdf
  - field: filters
    text: Add Field
  - field: email
    text: name@email.com
  - field: updateFields
    text: Add Field
  - field: Line
    text: Add Line Item Property
  - field: additionalFields
    text: Add Field
  - field: fileName
    text: data.pdf
  - field: filters
    text: Add Field
  - field: email
    text: name@email.com
  - field: updateFields
    text: Add Field
  - field: filters
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: fileName
    text: data.pdf
  - field: filters
    text: Add Field
  - field: email
    text: name@email.com
  - field: updateFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: filters
    text: Add Field
  - field: updateFields
    text: Add Field
  - field: filters
    text: Add Field
  hints:
  - field: binaryProperty
    text: The name of the output binary field to put the file in
  - field: binaryProperty
    text: The name of the output binary field to put the file in
  - field: binaryProperty
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
  "$id": "https://n8n.io/schemas/nodes/quickbooks.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "QuickBooks Online Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "getReport",
        "create",
        "delete",
        "get",
        "getAll",
        "update",
        "send",
        "void"
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
            "bill",
            "customer",
            "employee",
            "estimate",
            "invoice",
            "item",
            "payment",
            "purchase",
            "transaction",
            "vendor"
          ],
          "default": "customer"
        },
        "operation": {
          "description": "",
          "type": "string",
          "enum": [
            "get",
            "getAll"
          ],
          "default": "get"
        },
        "simple": {
          "description": "Whether to return a simplified version of the response instead of the raw data",
          "type": "boolean",
          "default": true
        },
        "filters": {
          "description": "The condition for selecting purchases. See the <a href=\"https://developer.intuit.com/app/developer/qbo/docs/develop/explore-the-quickbooks-online-api/data-queries\">guide</a> for supported syntax.",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "VendorRef": {
          "description": "The ID of the vendor who the bill is for. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "Line": {
          "description": "Individual line item of a transaction",
          "type": "string",
          "default": {},
          "examples": [
            "Add Line Item Property"
          ]
        },
        "additionalFields": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "billId": {
          "description": "The ID of the bill to update",
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
        "updateFields": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "displayName": {
          "description": "The display name of the vendor to create",
          "type": "string",
          "default": ""
        },
        "customerId": {
          "description": "The ID of the customer to update",
          "type": "string",
          "default": ""
        },
        "FamilyName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "GivenName": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "employeeId": {
          "description": "The ID of the employee to update",
          "type": "string",
          "default": ""
        },
        "CustomerRef": {
          "description": "The ID of the customer who the payment is for. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>.",
          "type": "string",
          "default": []
        },
        "estimateId": {
          "description": "The ID of the estimate to update",
          "type": "string",
          "default": ""
        },
        "download": {
          "description": "Whether to download estimate as PDF file",
          "type": "boolean",
          "default": false
        },
        "binaryProperty": {
          "description": "",
          "type": "string",
          "default": "data"
        },
        "fileName": {
          "description": "Name of the file that will be downloaded",
          "type": "string",
          "default": "",
          "examples": [
            "data.pdf"
          ]
        },
        "email": {
          "description": "The email of the recipient of the payment",
          "type": "string",
          "default": "",
          "format": "email",
          "examples": [
            "name@email.com"
          ]
        },
        "invoiceId": {
          "description": "The ID of the invoice to update",
          "type": "string",
          "default": ""
        },
        "itemId": {
          "description": "The ID of the item to retrieve",
          "type": "string",
          "default": ""
        },
        "TotalAmt": {
          "description": "Total amount of the transaction",
          "type": "number",
          "default": 0
        },
        "paymentId": {
          "description": "The ID of the payment to update",
          "type": "string",
          "default": ""
        },
        "vendorId": {
          "description": "The ID of the vendor to update",
          "type": "string",
          "default": ""
        },
        "purchaseId": {
          "description": "The ID of the purchase to retrieve",
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
      "name": "quickBooksOAuth2Api",
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
