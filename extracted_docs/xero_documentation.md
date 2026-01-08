---
title: "Node: Xero"
slug: "node-xero"
version: "1"
updated: "2026-01-08"
summary: "Consume Xero API"
node_type: "regular"
group: "['output']"
---

# Node: Xero

**Purpose.** Consume Xero API
**Subtitle.** ={{$parameter["operation"] + ": " + $parameter["resource"]}}


---

## Node Details

- **Icon:** `file:xero.svg`
- **Group:** `['output']`
- **Inputs:** `['Main']`
- **Outputs:** `['Main']`

---

## Authentication

- **xeroOAuth2Api**: N/A


---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `xeroOAuth2Api` | ✓ | - |

---

## API Patterns

**Headers Used:** Content-Type

---

## Operations

### Contact Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a contact |
| Get | `get` | Get a contact |
| Get Many | `getAll` | Get many contacts |
| Update | `update` | Update a contact |

### Invoice Resource Operations

| Operation | ID | Description |
| --------- | -- | ----------- |
| Create | `create` | Create a invoice |
| Get | `get` | Get a invoice |
| Get Many | `getAll` | Get many invoices |
| Update | `update` | Update a invoice |

---

## Parameters

### Resource Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Resource | `resource` | options | invoice | ✗ | Resource to operate on |  |

**Resource options:**

* **Contact** (`contact`)
* **Invoice** (`invoice`)

---

### Operation Selector

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Operation | `operation` | options | create | ✗ | Create a contact |  |

**Operation options:**

* **Create** (`create`) - Create a contact
* **Get** (`get`) - Get a contact
* **Get Many** (`getAll`) - Get many contacts
* **Update** (`update`) - Update a contact

---

### Create parameters (`create`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Organization Name or ID | `organizationId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Name | `name` | string |  | ✓ | Full name of contact/organisation |  |
| Additional Fields | `additionalFields` | collection | {} | ✗ | A user defined account number | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Number | `accountNumber` | string |  | A user defined account number |
| Addresses | `addressesUi` | fixedCollection | {} |  |
| Bank Account Details | `bankAccountDetails` | string |  | Bank account number of contact |
| Contact Number | `contactNumber` | string |  | This field is read only on the Xero contact screen, used to identify contacts in external systems |
| Contact Status | `contactStatus` | options |  | The Contact is active and can be used in transactions |
| Default Currency | `defaultCurrency` | string |  | Default currency for raising invoices against contact |
| Email | `emailAddress` | string |  | Email address of contact person (umlauts not supported) (max length = 255) |
| First Name | `firstName` | string |  | First name of contact person (max length = 255) |
| Last Name | `lastName` | string |  | Last name of contact person (max length = 255) |
| Phones | `phonesUi` | fixedCollection | {} |  |
| Purchase Default Account Code Name or ID | `purchasesDefaultAccountCode` | options |  | The default purchases account code for contacts. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Sales Default Account Code Name or ID | `salesDefaultAccountCode` | options |  | The default sales account code for contacts. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Skype | `skypeUserName` | string |  | Skype user name of contact |
| Tax Number | `taxNumber` | string |  | Tax number of contact |
| Xero Network Key | `xeroNetworkKey` | string |  | Store XeroNetworkKey for contacts |

</details>

| Organization Name or ID | `organizationId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Type | `type` | options |  | ✓ | Accounts Payable or supplier invoice |  |

**Type options:**

* **Bill** (`ACCPAY`) - Accounts Payable or supplier invoice
* **Sales Invoice** (`ACCREC`) - Accounts Receivable or customer invoice

| Contact ID | `contactId` | string |  | ✓ |  |  |
| Line Items | `lineItemsUi` | fixedCollection | {} | ✓ | Line item data | e.g. Add Line Item |  |

<details>
<summary><strong>Line Items sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Line Item | `lineItemsValues` |  |  |  |

</details>

| Additional Fields | `additionalFields` | collection | {} | ✗ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Additional Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Branding Theme Name or ID | `brandingThemeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Currency Name or ID | `currency` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Currency Rate | `currencyRate` | string |  | The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used. |
| Date | `date` | dateTime |  | Date invoice was issued - YYYY-MM-DD. If the Date element is not specified it will default to the current date based on the timezone setting of the organisation. |
| Due Date | `dueDate` | dateTime |  | Date invoice is due - YYYY-MM-DD |
| Expected Payment Date | `expectedPaymentDate` | dateTime |  | Shown on sales invoices (Accounts Receivable) when this has been set |
| Invoice Number | `invoiceNumber` | string |  |  |
| Line Amount Type | `lineAmountType` | options | Exclusive | Line items are exclusive of tax |
| Planned Payment Date | `plannedPaymentDate` | dateTime |  | Shown on bills (Accounts Payable) when this has been set |
| Reference | `reference` | string |  | ACCREC only - additional reference number (max length = 255) |
| Send To Contact | `sendToContact` | boolean | False | Whether the invoice in the Xero app should be marked as "sent". This can be set only on invoices that have been approved. |
| Status | `status` | options | DRAFT |  |
| URL | `url` | string |  | URL link to a source document - shown as "Go to [appName]" in the Xero app |

</details>


### Get parameters (`get`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Organization Name or ID | `organizationId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Contact ID | `contactId` | string |  | ✓ |  |  |
| Organization Name or ID | `organizationId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Invoice ID | `invoiceId` | string |  | ✓ |  |  |

### Get Many parameters (`getAll`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Organization Name or ID | `organizationId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | Whether contacts with a status of ARCHIVED will be included in the response | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Include Archived | `includeArchived` | boolean | False | Whether contacts with a status of ARCHIVED will be included in the response |
| Order By | `orderBy` | string |  | Order by any element returned |
| Sort Order | `sortOrder` | options |  |  |
| Where | `where` | string |  | The where parameter allows you to filter on endpoints and elements that don't have explicit parameters. <a href="https://developer.xero.com/documentation/api/requests-and-responses#get-modified">Examples Here</a>. |

</details>

| Organization Name or ID | `organizationId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Return All | `returnAll` | boolean | False | ✗ | Whether to return all results or only up to a given limit |  |
| Limit | `limit` | number | 100 | ✗ | Max number of results to return | min:1, max:100 |
| Options | `options` | collection | {} | ✗ | Whether you'll only retrieve Invoices created by your app | e.g. Add option |  |

<details>
<summary><strong>Options sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Created By My App | `createdByMyApp` | boolean | False | Whether you'll only retrieve Invoices created by your app |
| Order By | `orderBy` | string |  | Order by any element returned |
| Sort Order | `sortOrder` | options |  |  |
| Statuses | `statuses` | multiOptions | [] |  |
| Where | `where` | string |  | The where parameter allows you to filter on endpoints and elements that don't have explicit parameters. <a href="https://developer.xero.com/documentation/api/requests-and-responses#get-modified">Examples Here</a>. |

</details>


### Update parameters (`update`)

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Organization Name or ID | `organizationId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Contact ID | `contactId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✗ | A user defined account number | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Account Number | `accountNumber` | string |  | A user defined account number |
| Addresses | `addressesUi` | fixedCollection | {} |  |
| Bank Account Details | `bankAccountDetails` | string |  | Bank account number of contact |
| Contact Number | `contactNumber` | string |  | This field is read only on the Xero contact screen, used to identify contacts in external systems |
| Contact Status | `contactStatus` | options |  | The Contact is active and can be used in transactions |
| Default Currency | `defaultCurrency` | string |  | Default currency for raising invoices against contact |
| Email | `emailAddress` | string |  | Email address of contact person (umlauts not supported) (max length = 255) |
| First Name | `firstName` | string |  | First name of contact person (max length = 255) |
| Last Name | `lastName` | string |  | Last name of contact person (max length = 255) |
| Name | `name` | string |  | Full name of contact/organisation |
| Phones | `phonesUi` | fixedCollection | {} |  |
| Purchase Default Account Code Name or ID | `purchasesDefaultAccountCode` | options |  | The default purchases account code for contacts. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Sales Default Account Code Name or ID | `salesDefaultAccountCode` | options |  | The default sales account code for contacts. Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>. |
| Skype | `skypeUserName` | string |  | Skype user name of contact |
| Tax Number | `taxNumber` | string |  | Tax number of contact |
| Xero Network Key | `xeroNetworkKey` | string |  | Store XeroNetworkKey for contacts |

</details>

| Organization Name or ID | `organizationId` | options |  | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |  |
| Invoice ID | `invoiceId` | string |  | ✓ |  |  |
| Update Fields | `updateFields` | collection | {} | ✓ | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> | e.g. Add Field |  |

<details>
<summary><strong>Update Fields sub-options</strong></summary>

| Sub-Option | Field ID | Type | Default | Description |
| ---------- | -------- | ---- | ------- | ----------- |
| Branding Theme Name or ID | `brandingThemeId` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Contact ID | `contactId` | string |  |  |
| Currency Name or ID | `currency` | options |  | Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a> |
| Currency Rate | `currencyRate` | string |  | The currency rate for a multicurrency invoice. If no rate is specified, the XE.com day rate is used. |
| Date | `date` | dateTime |  | Date invoice was issued - YYYY-MM-DD. If the Date element is not specified it will default to the current date based on the timezone setting of the organisation. |
| Due Date | `dueDate` | dateTime |  | Date invoice is due - YYYY-MM-DD |
| Expected Payment Date | `expectedPaymentDate` | dateTime |  | Shown on sales invoices (Accounts Receivable) when this has been set |
| Invoice Number | `invoiceNumber` | string |  |  |
| Line Amount Type | `lineAmountType` | options | Exclusive | Line items are exclusive of tax |
| Line Items | `lineItemsUi` | fixedCollection | {} | Line item data |
| Planned Payment Date | `plannedPaymentDate` | dateTime |  | Shown on bills (Accounts Payable) when this has been set |
| Reference | `reference` | string |  | ACCREC only - additional reference number (max length = 255) |
| Send To Contact | `sendToContact` | boolean | False | Whether the invoice in the Xero app should be marked as "sent". This can be set only on invoices that have been approved. |
| Status | `status` | options | DRAFT |  |
| URL | `url` | string |  | URL link to a source document - shown as "Go to [appName]" in the Xero app |

</details>


---

## Load Options Methods

- `getItemCodes`

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
node: xero
displayName: Xero
description: Consume Xero API
version: '1'
nodeType: regular
group:
- output
credentials:
- name: xeroOAuth2Api
  required: true
operations:
- id: create
  name: Create
  description: Create a contact
  params:
  - id: organizationId
    name: Organization Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: &id001
      required: true
      displayOptions:
        show:
          resource:
          - invoice
          operation:
          - getAll
    typeInfo: &id002
      type: options
      displayName: Organization Name or ID
      name: organizationId
      typeOptions:
        loadOptionsMethod: getTenants
      possibleValues: []
  - id: name
    name: Name
    type: string
    default: ''
    required: true
    description: Full name of contact/organisation
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
      displayName: Name
      name: name
  - id: organizationId
    name: Organization Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: type
    name: Type
    type: options
    default: ''
    required: true
    description: Accounts Payable or supplier invoice
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - invoice
          operation:
          - create
    typeInfo:
      type: options
      displayName: Type
      name: type
      possibleValues:
      - value: ACCPAY
        name: Bill
        description: Accounts Payable or supplier invoice
      - value: ACCREC
        name: Sales Invoice
        description: Accounts Receivable or customer invoice
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id003
      required: true
      displayOptions:
        show:
          resource:
          - invoice
          operation:
          - create
    typeInfo: &id004
      type: string
      displayName: Contact ID
      name: contactId
  - id: lineItemsUi
    name: Line Items
    type: fixedCollection
    default: {}
    required: true
    description: Line item data
    placeholder: Add Line Item
    validation:
      required: true
      displayOptions:
        show:
          resource:
          - invoice
          operation:
          - create
    typeInfo:
      type: fixedCollection
      displayName: Line Items
      name: lineItemsUi
      typeOptions:
        multipleValues: true
      subProperties:
      - name: lineItemsValues
        displayName: Line Item
        values:
        - displayName: Description
          name: description
          type: string
          description: A line item with just a description
          default: ''
        - displayName: Quantity
          name: quantity
          type: number
          description: LineItem Quantity
          default: 1
          typeOptions:
            minValue: 1
        - displayName: Unit Amount
          name: unitAmount
          type: string
          description: Lineitem unit amount. By default, unit amount will be rounded
            to two decimal places.
          default: ''
        - displayName: Item Code Name or ID
          name: itemCode
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getItemCodes
        - displayName: Account Code Name or ID
          name: accountCode
          type: options
          description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
          default: ''
          typeOptions:
            loadOptionsMethod: getAccountCodes
        - displayName: Tax Type
          name: taxType
          type: options
          value: INPUT
          default: ''
          required: true
          options:
          - name: Tax on Purchases
            value: INPUT
            displayName: Tax On Purchases
          - name: Tax Exempt
            value: NONE
            displayName: Tax Exempt
          - name: Tax on Sales
            value: OUTPUT
            displayName: Tax On Sales
          - name: Sales Tax on Imports
            value: GSTONIMPORTS
            displayName: Sales Tax On Imports
        - displayName: Tax Amount
          name: taxAmount
          type: string
          description: The tax amount is auto calculated as a percentage of the line
            amount based on the tax rate
          default: ''
        - displayName: Line Amount
          name: lineAmount
          type: string
          description: The line amount reflects the discounted price if a DiscountRate
            has been used
          default: ''
        - displayName: Discount Rate
          name: discountRate
          type: string
          description: Percentage discount or discount amount being applied to a line
            item. Only supported on ACCREC invoices - ACCPAY invoices and credit notes
            in Xero do not support discounts.
          default: ''
        - displayName: Tracking
          name: trackingUi
          type: fixedCollection
          description: Any LineItem can have a maximum of 2 TrackingCategory elements.
          placeholder: Add Tracking
          default: {}
          options:
          - name: trackingValues
            displayName: Tracking
            values:
            - displayName: Name
              name: name
              type: options
              description: Name of the tracking category
              default: ''
              typeOptions:
                loadOptionsMethod: getTrakingCategories
            - displayName: Option
              name: option
              type: options
              description: Name of the option
              default: ''
              typeOptions:
                loadOptionsMethod: getTrakingOptions
          typeOptions:
            multipleValues: true
- id: get
  name: Get
  description: Get a contact
  params:
  - id: organizationId
    name: Organization Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: organizationId
    name: Organization Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: invoiceId
    name: Invoice ID
    type: string
    default: ''
    required: true
    description: ''
    validation: &id009
      required: true
      displayOptions:
        show:
          resource:
          - invoice
          operation:
          - get
    typeInfo: &id010
      type: string
      displayName: Invoice ID
      name: invoiceId
- id: getAll
  name: Get Many
  description: Get many contacts
  params:
  - id: organizationId
    name: Organization Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: &id005
      displayOptions:
        show:
          resource:
          - invoice
          operation:
          - getAll
    typeInfo: &id006
      type: boolean
      displayName: Return All
      name: returnAll
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: &id007
      displayOptions:
        show:
          resource:
          - invoice
          operation:
          - getAll
          returnAll:
          - false
    typeInfo: &id008
      type: number
      displayName: Limit
      name: limit
      typeOptions:
        minValue: 1
        maxValue: 100
  - id: organizationId
    name: Organization Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: returnAll
    name: Return All
    type: boolean
    default: false
    required: false
    description: Whether to return all results or only up to a given limit
    validation: *id005
    typeInfo: *id006
  - id: limit
    name: Limit
    type: number
    default: 100
    required: false
    description: Max number of results to return
    validation: *id007
    typeInfo: *id008
- id: update
  name: Update
  description: Update a contact
  params:
  - id: organizationId
    name: Organization Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: contactId
    name: Contact ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id003
    typeInfo: *id004
  - id: organizationId
    name: Organization Name or ID
    type: options
    default: ''
    required: true
    description: Choose from the list, or specify an ID using an <a href="https://docs.n8n.io/code/expressions/">expression</a>
    validation: *id001
    typeInfo: *id002
  - id: invoiceId
    name: Invoice ID
    type: string
    default: ''
    required: true
    description: ''
    validation: *id009
    typeInfo: *id010
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
  - field: options
    text: Add option
  - field: updateFields
    text: Add Field
  - field: lineItemsUi
    text: Add Line Item
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
  "$id": "https://n8n.io/schemas/nodes/xero.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Xero Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "operation": {
      "type": "string",
      "enum": [
        "create",
        "get",
        "getAll",
        "update"
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
            "contact",
            "invoice"
          ],
          "default": "invoice"
        },
        "operation": {
          "description": "Create a invoice",
          "type": "string",
          "enum": [
            "create",
            "get",
            "getAll",
            "update"
          ],
          "default": "create"
        },
        "organizationId": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": ""
        },
        "name": {
          "description": "Full name of contact/organisation",
          "type": "string",
          "default": ""
        },
        "additionalFields": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "contactId": {
          "description": "",
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
          "default": 100
        },
        "options": {
          "description": "Whether you'll only retrieve Invoices created by your app",
          "type": "string",
          "default": {},
          "examples": [
            "Add option"
          ]
        },
        "updateFields": {
          "description": "Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code/expressions/\">expression</a>",
          "type": "string",
          "default": {},
          "examples": [
            "Add Field"
          ]
        },
        "type": {
          "description": "Accounts Payable or supplier invoice",
          "type": "string",
          "enum": [
            "ACCPAY",
            "ACCREC"
          ],
          "default": ""
        },
        "lineItemsUi": {
          "description": "Line item data",
          "type": "string",
          "default": {},
          "examples": [
            "Add Line Item"
          ]
        },
        "invoiceId": {
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
      "name": "xeroOAuth2Api",
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
