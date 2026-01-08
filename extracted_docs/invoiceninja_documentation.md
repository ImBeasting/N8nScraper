---
title: "Node: Invoice Ninja"
slug: "node-invoiceninja"
version: "['1', '2']"
updated: "2026-01-08"
summary: "Consume Invoice Ninja API"
node_type: "regular"
group: "['output']"
---

# Node: Invoice Ninja

**Purpose.** Consume Invoice Ninja API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:invoiceNinja.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **invoiceNinjaApi**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `invoiceNinjaApi` | ✓ | - |

---

## Operations

### Client Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new client |
| Delete | `delete` | Delete a client |
| Get | `get` | Get data of a client |
| Get Many | `getAll` | Get data of many clients |

### Invoice Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new invoice |
| Delete | `delete` | Delete a invoice |
| Email | `email` | Email an invoice |
| Get | `get` | Get data of a invoice |
| Get Many | `getAll` | Get data of many invoices |

### Task Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new task |
| Delete | `delete` | Delete a task |
| Get | `get` | Get data of a task |
| Get Many | `getAll` | Get data of many tasks |

### Payment Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new payment |
| Delete | `delete` | Delete a payment |
| Get | `get` | Get data of a payment |
| Get Many | `getAll` | Get data of many payments |

### Expense Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new expense |
| Delete | `delete` | Delete an expense |
| Get | `get` | Get data of an expense |
| Get Many | `getAll` | Get data of many expenses |

### Quote Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new quote |
| Delete | `delete` | Delete a quote |
| Email | `email` | Email a quote |
| Get | `get` | Get data of a quote |
| Get Many | `getAll` | Get data of many quotes |

### Bank_Transaction Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a new bank transaction |
| Delete | `delete` | Delete a bank transaction |
| Get | `get` | Get data of a bank transaction |
| Get Many | `getAll` | Get data of many bank transactions |
| Match Payment | `matchPayment` | Match payment to a bank transaction |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | client | ✗ | Resource to operate on |  |
---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a new client |  |

**Operation options:**

* **Create** (`create`) - Create a new client
* **Delete** (`delete`) - Delete a client
* **Get** (`get`) - Get data of a client
* **Get Many** (`getAll`) - Get data of many clients

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Client Name | `clientName` | string |  |  |
| ID Number | `idNumber` | string |  |  |
| Private Notes | `privateNotes` | string |  |  |
| VAT Number | `vatNumber` | string |  |  |
| Work Phone | `workPhone` | string |  |  |
| Website | `website` | string |  |  |

</details>

| Billing Address | `billingAddressUi` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Billing Address |  |

<details>
<summary><strong>Billing Address sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Billing Address | `billingAddressValue` |  |  |  |

</details>

| Contacts | `contactsUi` | fixedCollection | {} | ✗ | e.g. Add Contact |  |

<details>
<summary><strong>Contacts sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Contact | `contacstValues` |  |  |  |

</details>

| Shipping Address | `shippingAddressUi` | fixedCollection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Shipping Address |  |

<details>
<summary><strong>Shipping Address sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Shipping Address | `shippingAddressValue` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Client Name or ID | `client` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Auto Bill | `autoBill` | boolean | False |  |
| Custom Value 1 | `customValue1` | number | 0 |  |
| Custom Value 2 | `customValue2` | number | 0 |  |
| Discount | `discount` | string |  |  |
| Due Date | `dueDate` | dateTime |  |  |
| Email | `email` | string |  |  |
| Email Invoice | `emailInvoice` | boolean | False |  |
| Invoice Date | `invoiceDate` | dateTime |  |  |
| Invoice Number | `invoiceNumber` | string |  |  |
| Invoice Status | `invoiceStatus` | options | 1 |  |
| Is Amount Discount | `isAmountDiscount` | boolean | False |  |
| Mark Sent | `markSent` | boolean | False |  |
| Paid | `paid` | number | 0 |  |
| Partial | `partial` | number | 0 |  |
| Partial Due Date | `partialDueDate` | dateTime |  |  |
| PO Number | `poNumber` | string |  |  |
| Private Notes | `privateNotes` | string |  |  |
| Public Notes | `publicNotes` | string |  |  |
| Tax Name 1 | `taxName1` | string |  |  |
| Tax Name 2 | `taxName2` | string |  |  |
| Tax Rate 1 | `taxRate1` | number | 0 |  |
| Tax Rate 2 | `taxRate2` | number | 0 |  |

</details>

| Invoice Items | `invoiceItemsUi` | fixedCollection | {} | ✗ | e.g. Add Invoice Item |  |

<details>
<summary><strong>Invoice Items sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Invoice Item | `invoiceItemsValues` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Client Name or ID | `client` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Custom Value 1 | `customValue1` | string |  |  |
| Custom Value 2 | `customValue2` | string |  |  |
| Description | `description` | string |  |  |
| Project Name or ID | `project` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Time Logs | `timeLogsUi` | fixedCollection | {} | ✗ | e.g. Add Time Log |  |

<details>
<summary><strong>Time Logs sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Time Log | `timeLogsValues` |  |  |  |

</details>

| Invoice Name or ID | `invoice` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Amount | `amount` | number | 0 | ✗ |  | min:0, max:∞ |
| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Payment Type | `paymentType` | options | 1 |  |
| Transfer Reference | `transferReference` | string |  |  |
| Private Notes | `privateNotes` | string |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Payment Type | `paymentType` | options | 1 |  |
| Transfer Reference | `transferReference` | string |  |  |
| Private Notes | `privateNotes` | string |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Amount | `amount` | number | 0 |  |
| Billable | `billable` | boolean | False |  |
| Client Name or ID | `client` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Custom Value 1 | `customValue1` | string |  |  |
| Custom Value 2 | `customValue2` | string |  |  |
| Category Name or ID | `category` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Expense Date | `expenseDate` | dateTime |  |  |
| Payment Date | `paymentDate` | dateTime |  |  |
| Payment Type | `paymentType` | options | 1 |  |
| Private Notes | `privateNotes` | string |  |  |
| Public Notes | `publicNotes` | string |  |  |
| Tax Name 1 | `taxName1` | string |  |  |
| Tax Name 2 | `taxName2` | string |  |  |
| Tax Rate 1 | `taxRate1` | number | 0 |  |
| Tax Rate 2 | `taxRate2` | number | 0 |  |
| Transaction Reference | `transactionReference` | string |  |  |
| Vendor Name or ID | `vendor` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Amount | `amount` | number | 0 |  |
| Billable | `billable` | boolean | False |  |
| Client Name or ID | `client` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Custom Value 1 | `customValue1` | string |  |  |
| Custom Value 2 | `customValue2` | string |  |  |
| Category Name or ID | `category` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Expense Date | `expenseDate` | dateTime |  |  |
| Payment Date | `paymentDate` | dateTime |  |  |
| Payment Type | `paymentType` | options | 1 |  |
| Private Notes | `privateNotes` | string |  |  |
| Public Notes | `publicNotes` | string |  |  |
| Tax Name 1 | `taxName1` | string |  |  |
| Tax Name 2 | `taxName2` | string |  |  |
| Tax Rate 1 | `taxRate1` | number | 0 |  |
| Tax Rate 2 | `taxRate2` | number | 0 |  |
| Transaction Reference | `transactionReference` | string |  |  |
| Vendor Name or ID | `vendor` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Client Name or ID | `client` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Auto Bill | `autoBill` | boolean | False |  |
| Custom Value 1 | `customValue1` | number | 0 |  |
| Custom Value 2 | `customValue2` | number | 0 |  |
| Discount | `discount` | string |  |  |
| Due Date | `dueDate` | dateTime |  |  |
| Email | `email` | string |  |  |
| Email Quote | `emailQuote` | boolean | False |  |
| Quote Date | `quoteDate` | dateTime |  |  |
| Quote Number | `quoteNumber` | string |  |  |
| Quote Status | `quoteStatus` | options | 1 |  |
| Is Amount Discount | `isAmountDiscount` | boolean | False |  |
| Paid | `paid` | number | 0 |  |
| Partial | `partial` | number | 0 |  |
| Partial Due Date | `partialDueDate` | dateTime |  |  |
| Po Number | `poNumber` | string |  |  |
| Private Notes | `privateNotes` | string |  |  |
| Public Notes | `publicNotes` | string |  |  |
| Tax Name 1 | `taxName1` | string |  |  |
| Tax Name 2 | `taxName2` | string |  |  |
| Tax Rate 1 | `taxRate1` | number | 0 |  |
| Tax Rate 2 | `taxRate2` | number | 0 |  |

</details>

| Invoice Items | `invoiceItemsUi` | fixedCollection | {} | ✗ | e.g. Add Invoice Item |  |

<details>
<summary><strong>Invoice Items sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Invoice Item | `invoiceItemsValues` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Amount | `amount` | number | 0 |  |
| Bank Integration Name or ID | `bankIntegrationId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Base Type | `baseType` | options |  |  |
| Currency Name or ID | `currencyId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Date | `date` | dateTime |  |  |
| Description | `description` | string |  |  |

</details>


### Delete parameters (`delete`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Client ID | `clientId` | string |  | ✓ |  |  |
| Invoice ID | `invoiceId` | string |  | ✓ |  |  |
| Task ID | `taskId` | string |  | ✓ |  |  |
| Payment ID | `paymentId` | string |  | ✓ |  |  |
| Expense ID | `expenseId` | string |  | ✓ |  |  |
| Quote ID | `quoteId` | string |  | ✓ |  |  |
| Bank Transaction ID | `bankTransactionId` | string |  | ✓ |  |  |

### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Client ID | `clientId` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include | `include` | options | invoices |  |

</details>

| Invoice ID | `invoiceId` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include | `include` | options | client |  |

</details>

| Task ID | `taskId` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include | `include` | options | client |  |

</details>

| Payment ID | `paymentId` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include | `include` | options | client |  |

</details>

| Expense ID | `expenseId` | string |  | ✓ |  |  |
| Quote ID | `quoteId` | string |  | ✓ |  |  |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include | `include` | options | client |  |

</details>

| Bank Transaction ID | `bankTransactionId` | string |  | ✓ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:60 |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include | `include` | options | invoices |  |
| Status | `status` | options | active |  |
| Created At | `createdAt` | dateTime |  |  |
| Updated At | `updatedAt` | dateTime |  |  |
| Is Deleted | `isDeleted` | boolean | False |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:60 |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Invoice Number | `invoiceNumber` | string |  |  |
| Include | `include` | options | client |  |
| Status | `status` | options | active |  |
| Created At | `createdAt` | dateTime |  |  |
| Updated At | `updatedAt` | dateTime |  |  |
| Is Deleted | `isDeleted` | boolean | False |  |
| Client Status | `clientStatus` | options | all |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:60 |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include | `include` | options | client |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:60 |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include | `include` | options | client |  |
| Status | `status` | options | active |  |
| Created At | `createdAt` | dateTime |  |  |
| Updated At | `updatedAt` | dateTime |  |  |
| Is Deleted | `isDeleted` | boolean | False |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:60 |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:60 |
| Options | `options` | collection | {} | ✗ | e.g. Add Field |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Quote Number | `quoteNumber` | string |  |  |
| Include | `include` | options | client |  |
| Status | `status` | options | active |  |
| Created At | `createdAt` | dateTime |  |  |
| Updated At | `updatedAt` | dateTime |  |  |
| Is Deleted | `isDeleted` | boolean | False |  |

</details>

| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 50 | ✗ | Max number of results to return | min:1, max:60 |

### Email parameters (`email`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Invoice ID | `invoiceId` | string |  | ✓ |  |  |
| Quote ID | `quoteId` | string |  | ✓ |  |  |

### Match Payment parameters (`matchPayment`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Bank Transaction ID | `bankTransactionId` | string |  | ✓ |  |  |
| Payment Name or ID | `paymentId` | options |  | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |

---

## Load Options Methods

- `getClients`
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
* Categories: Finance & Accounting

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: invoiceNinja
displayName: Invoice Ninja
description: Consume Invoice Ninja API
version:
- '1'
- '2'
nodeType: regular
group:
- output
credentials:
- name: invoiceNinjaApi
  required: true
operations:
- id: create
  name: Create
  description: Create a new client
  params:
  - id: billingAddressUi
    name: Billing Address
    type: fixedCollection
    default: {}
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Billing Address
    validation:
      displayOptions:
        show:
          resource:
          - client
          operation:
          - create
    typeInfo:
      type: fixedCollection
      displayName: Billing Address
      name: billingAddressUi
      typeOptions:
        multipleValues: false
      subProperties:
      - name: billingAddressValue
        displayName: Billing Address
        values:
        - displayName: Street Address
          name: streetAddress
          type: string
          default: ''
        - displayName: Apt/Suite
          name: aptSuite
          type: string
          default: ''
        - displayName: City
          name: city
          type: string
          default: ''
        - displayName: State
          name: state
          type: string
          default: ''
        - displayName: Postal Code
          name: postalCode
          type: string
          default: ''
        - displayName: Country Code Name or ID
          name: countryCode
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getCountryCodes
  - id: contactsUi
    name: Contacts
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Contact
    validation:
      displayOptions:
        show:
          resource:
          - client
          operation:
          - create
    typeInfo:
      type: fixedCollection
      displayName: Contacts
      name: contactsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: contacstValues
        displayName: Contact
        values:
        - displayName: First Name
          name: firstName
          type: string
          default: ''
        - displayName: Last Name
          name: lastName
          type: string
          default: ''
        - displayName: Email
          name: email
          type: string
          placeholder: name@email.com
          default: ''
        - displayName: Phone
          name: phone
          type: string
          default: ''
  - id: shippingAddressUi
    name: Shipping Address
    type: fixedCollection
    default: {}
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    placeholder: Add Shipping Address
    validation:
      displayOptions:
        show:
          resource:
          - client
          operation:
          - create
    typeInfo:
      type: fixedCollection
      displayName: Shipping Address
      name: shippingAddressUi
      typeOptions:
        multipleValues: false
      subProperties:
      - name: shippingAddressValue
        displayName: Shipping Address
        values:
        - displayName: Street Address
          name: streetAddress
          type: string
          default: ''
        - displayName: Apt/Suite
          name: aptSuite
          type: string
          default: ''
        - displayName: City
          name: city
          type: string
          default: ''
        - displayName: State
          name: state
          type: string
          default: ''
        - displayName: Postal Code
          name: postalCode
          type: string
          default: ''
        - displayName: Country Code Name or ID
          name: countryCode
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getCountryCodes
  - id: invoiceItemsUi
    name: Invoice Items
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Invoice Item
    validation: &id001
      displayOptions:
        show:
          resource:
          - quote
          operation:
          - create
    typeInfo: &id002
      type: fixedCollection
      displayName: Invoice Items
      name: invoiceItemsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: invoiceItemsValues
        displayName: Invoice Item
        values:
        - displayName: Cost
          name: cost
          type: number
          default: 0
        - displayName: Description
          name: description
          type: string
          default: ''
        - displayName: Service
          name: service
          type: string
          default: ''
        - displayName: Hours
          name: hours
          type: number
          default: 0
          typeOptions:
            minValue: 0
        - displayName: Tax Name 1
          name: taxName1
          type: string
          default: ''
        - displayName: Tax Name 2
          name: taxName2
          type: string
          default: ''
        - displayName: Tax Rate 1
          name: taxRate1
          type: number
          default: 0
        - displayName: Tax Rate 2
          name: taxRate2
          type: number
          default: 0
  - id: timeLogsUi
    name: Time Logs
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Time Log
    validation:
      displayOptions:
        show:
          resource:
          - task
          operation:
          - create
    typeInfo:
      type: fixedCollection
      displayName: Time Logs
      name: timeLogsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: timeLogsValues
        displayName: Time Log
        values:
        - displayName: Start Date
          name: startDate
          type: dateTime
          default: ''
        - displayName: End Date
          name: endDate
          type: dateTime
          default: ''
        - displayName: Duration (Hours)
          name: duration
          type: number
          default: 0
          typeOptions:
            minValue: 0
  - id: invoice
    name: Invoice Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - payment
    typeInfo:
      type: options
      displayName: Invoice Name or ID
      name: invoice
      typeOptions:
        loadOptionsMethod: getInvoices
      possibleValues: []
  - id: amount
    name: Amount
    type: number
    default: 0
    required: false
    description: ''
    validation:
      displayOptions:
        show:
          operation:
          - create
          resource:
          - payment
    typeInfo:
      type: number
      displayName: Amount
      name: amount
      typeOptions:
        minValue: 0
  - id: invoiceItemsUi
    name: Invoice Items
    type: fixedCollection
    default: {}
    required: false
    description: ''
    placeholder: Add Invoice Item
    validation: *id001
    typeInfo: *id002
- id: delete
  name: Delete
  description: Delete a client
  params:
  - id: clientId
    name: Client ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - client
          operation:
          - get
    typeInfo: &id004
      type: string
      displayName: Client ID
      name: clientId
  - id: invoiceId
    name: Invoice ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id005
      required: true
      displayOptions:
        show:
          resource:
          - invoice
          operation:
          - get
    typeInfo: &id006
      type: string
      displayName: Invoice ID
      name: invoiceId
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id007
      required: true
      displayOptions:
        show:
          resource:
          - task
          operation:
          - get
    typeInfo: &id008
      type: string
      displayName: Task ID
      name: taskId
  - id: paymentId
    name: Payment ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id009
      displayOptions:
        show:
          resource:
          - bank_transaction
          operation:
          - matchPayment
    typeInfo: &id010
      type: options
      displayName: Payment Name or ID
      name: paymentId
      typeOptions:
        loadOptionsMethod: getPayments
      possibleValues: []
  - id: expenseId
    name: Expense ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id011
      required: true
      displayOptions:
        show:
          resource:
          - expense
          operation:
          - get
    typeInfo: &id012
      type: string
      displayName: Expense ID
      name: expenseId
  - id: quoteId
    name: Quote ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id013
      required: true
      displayOptions:
        show:
          resource:
          - quote
          operation:
          - get
    typeInfo: &id014
      type: string
      displayName: Quote ID
      name: quoteId
  - id: bankTransactionId
    name: Bank Transaction ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id015
      required: true
      displayOptions:
        show:
          resource:
          - bank_transaction
          operation:
          - matchPayment
    typeInfo: &id016
      type: string
      displayName: Bank Transaction ID
      name: bankTransactionId
- id: get
  name: Get
  description: Get data of a client
  params:
  - id: clientId
    name: Client ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: invoiceId
    name: Invoice ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: taskId
    name: Task ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id007
    typeInfo: *id008
  - id: paymentId
    name: Payment ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
  - id: expenseId
    name: Expense ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id011
    typeInfo: *id012
  - id: quoteId
    name: Quote ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id013
    typeInfo: *id014
  - id: bankTransactionId
    name: Bank Transaction ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id015
    typeInfo: *id016
- id: getAll
  name: Get Many
  description: Get data of many clients
  params:
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id017
      displayOptions:
        show:
          resource:
          - bank_transaction
          operation:
          - getAll
    typeInfo: &id018
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: &id019
      displayOptions:
        show:
          resource:
          - bank_transaction
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id020
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 60
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id017
    typeInfo: *id018
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id019
    typeInfo: *id020
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id017
    typeInfo: *id018
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id019
    typeInfo: *id020
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id017
    typeInfo: *id018
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id019
    typeInfo: *id020
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id017
    typeInfo: *id018
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id019
    typeInfo: *id020
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id017
    typeInfo: *id018
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id019
    typeInfo: *id020
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id017
    typeInfo: *id018
  - id: limit
    name: Limit
    type: number
    default: 50
    required: false
    description: Max number of results to return
    validation: *id019
    typeInfo: *id020
- id: email
  name: Email
  description: Email an invoice
  params:
  - id: invoiceId
    name: Invoice ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id005
    typeInfo: *id006
  - id: quoteId
    name: Quote ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id013
    typeInfo: *id014
- id: matchPayment
  name: Match Payment
  description: Match payment to a bank transaction
  params:
  - id: bankTransactionId
    name: Bank Transaction ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id015
    typeInfo: *id016
  - id: paymentId
    name: Payment Name or ID
    type: options
    default: ''
    required: false
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id009
    typeInfo: *id010
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
  - field: billingAddressUi
    text: Add Billing Address
  - field: contactsUi
    text: Add Contact
  - field: shippingAddressUi
    text: Add Shipping Address
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: invoiceItemsUi
    text: Add Invoice Item
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: timeLogsUi
    text: Add Time Log
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: additionalFields
    text: Add Field
  - field: invoiceItemsUi
    text: Add Invoice Item
  - field: options
    text: Add Field
  - field: options
    text: Add Field
  - field: additionalFields
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
  "$id": "https://n8n.io/schemas/nodes/invoiceNinja.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Invoice Ninja Node",
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
        "email",
        "matchPayment"
      ],
      "description": "Operation to perform"
    },
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "apiVersion": {
          "description": "",
          "type": "string",
          "enum": [
            "v4",
            "v5"
          ],
          "default": "v4"
        },
        "resource": {
          "description": "",
          "type": "string",
          "default": "client"
        },
        "operation": {
          "description": "Create a new bank transaction",
          "type": "string",
          "enum": [
            "create",
            "delete",
            "get",
            "getAll",
            "matchPayment"
          ],
          "default": "create"
        },
        "additionalFields": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "billingAddressUi": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Billing Address"
          ]
        },
        "contactsUi": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Contact"
          ]
        },
        "shippingAddressUi": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Shipping Address"
          ]
        },
        "clientId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "options": {
          "description": "",
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
        "invoiceItemsUi": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Invoice Item"
          ]
        },
        "invoiceId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "timeLogsUi": {
          "description": "",
          "type": "string",
          "default": {},
          "examples": [
            "Add Time Log"
          ]
        },
        "taskId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "invoice": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "amount": {
          "description": "",
          "type": "number",
          "default": 0
        },
        "paymentId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "expenseId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "quoteId": {
          "description": "",
          "type": "string",
          "default": ""
        },
        "bankTransactionId": {
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
    "version": [
      "1",
      "2"
    ]
  },
  "credentials": [
    {
      "name": "invoiceNinjaApi",
      "required": true
    }
  ]
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| ['1', '2'] | 2026-01-08 | Ultimate extraction with maximum detail for AI training |
