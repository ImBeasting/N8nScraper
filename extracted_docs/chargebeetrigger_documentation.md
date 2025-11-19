---
title: "Node: Chargebee Trigger"
slug: "node-chargebeetrigger"
version: "1"
updated: "2025-11-13"
summary: "Starts the workflow when Chargebee events occur"
node_type: "trigger"
group: "['trigger']"
---

# Node: Chargebee Trigger

**Purpose.** Starts the workflow when Chargebee events occur


---

## Node Details

- **Icon:** `file:chargebee.png`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`


---

## Trigger Properties

- **Event Trigger Description:** 
- **Activation Message:** 
- **Supports CORS:** False

---

## UI Tips & Notices

**Expression Mode Tip:** When using expressions (switching from Fixed to Expression mode), n8n displays:

> Anything inside `{{ }}` is JavaScript. [Learn more](https://docs.n8n.io/code-examples/expressions/)

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Events | `events` | multiOptions | [] | ✓ | Any time any event is triggered (Wildcard Event) |  |

**Events options:**

* ***** (`*`) - Any time any event is triggered (Wildcard Event)
* **Card Added** (`card_added`) - Triggered when a card is added for a customer
* **Card Deleted** (`card_deleted`) - Triggered when a card is deleted for a customer
* **Card Expired** (`card_expired`) - Triggered when the card for a customer has expired
* **Card Expiring** (`card_expiring`) - Triggered when the customer's credit card is expiring soon.Triggered 30 days before the expiry date
* **Card Updated** (`card_updated`) - Triggered when the card is updated for a customer
* **Customer Changed** (`customer_changed`) - Triggered when a customer is changed
* **Customer Created** (`customer_created`) - Triggered when a customer is created
* **Customer Deleted** (`customer_deleted`) - Triggered when a customer is deleted
* **Invoice Created** (`invoice_created`) - Event triggered (in the case of metered billing) when a 'Pending' invoice is created that has usage related charges or line items to be added, before being closed. This is triggered only when the “Notify for Pending Invoices” option is enabled.
* **Invoice Deleted** (`invoice_deleted`) - Event triggered when an invoice is deleted
* **Invoice Generated** (`invoice_generated`) - Event triggered when a new invoice is generated. In case of metered billing, this event is triggered when a 'Pending' invoice is closed.
* **Invoice Updated** (`invoice_updated`) - Triggered when the invoice’s shipping/billing address is updated, if the invoice is voided, or when the amount due is modified due to payments applied/removed
* **Payment Failed** (`payment_failed`) - Triggered when attempt to charge customer's credit card fails
* **Payment Initiated** (`payment_initiated`) - Triggered when a payment is initiated via direct debit
* **Payment Refunded** (`payment_refunded`) - Triggered when a payment refund is made
* **Payment Succeeded** (`payment_succeeded`) - Triggered when the payment is successfully collected
* **Refund Initiated** (`refund_initiated`) - Triggered when a refund is initiated via direct debit
* **Subscription Activated** (`subscription_activated`) - Triggered after the subscription has been moved from 'Trial' to 'Active' state
* **Subscription Cancellation Scheduled** (`subscription_cancellation_scheduled`) - Triggered when subscription is scheduled to cancel at end of current term
* **Subscription Cancelled** (`subscription_cancelled`) - Triggered when the subscription is cancelled. If it is cancelled due to non payment or because the card details are not present, the subscription will have the possible reason as 'cancel_reason'.
* **Subscription Cancelling** (`subscription_cancelling`) - Triggered 6 days prior to the scheduled cancellation date
* **Subscription Changed** (`subscription_changed`) - Triggered when the subscription's recurring items are changed
* **Subscription Created** (`subscription_created`) - Triggered when a new subscription is created
* **Subscription Deleted** (`subscription_deleted`) - Triggered when a subscription is deleted
* **Subscription Reactivated** (`subscription_reactivated`) - Triggered when the subscription is moved from cancelled state to 'Active' or 'Trial' state
* **Subscription Renewal Reminder** (`subscription_renewal_reminder`) - Triggered 3 days before each subscription's renewal
* **Subscription Renewed** (`subscription_renewed`) - Triggered when the subscription is renewed from the current term
* **Subscription Scheduled Cancellation Removed** (`subscription_scheduled_cancellation_removed`) - Triggered when scheduled cancellation is removed for the subscription
* **Subscription Shipping Address Updated** (`subscription_shipping_address_updated`) - Triggered when shipping address is added or updated for a subscription
* **Subscription Started** (`subscription_started`) - Triggered when a 'future' subscription gets started
* **Subscription Trial Ending** (`subscription_trial_ending`) - Triggered 6 days prior to the trial period's end date
* **Transaction Created** (`transaction_created`) - Triggered when a transaction is recorded
* **Transaction Deleted** (`transaction_deleted`) - Triggered when a transaction is deleted
* **Transaction Updated** (`transaction_updated`) - Triggered when a transaction is updated. E.g. (1) When a transaction is removed, (2) or when an excess payment is applied on an invoice, (3) or when amount_capturable gets updated.


---

## Execution Settings

**Note:** Trigger nodes have limited execution settings.

| Name | Field ID | Type | Default | Description |
| ---- | -------- | ---- | ------- | ----------- |
| Notes | `notes` | string |  | Optional note to save with the node |
| Display Note in Flow? | `notesInFlow` | boolean | False | If active, the note above will display in the flow as a subtitle |

---

## Notes & Caveats

* This node is part of n8n-nodes-base
* Categories: Finance & Accounting

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: chargebeeTrigger
displayName: Chargebee Trigger
description: Starts the workflow when Chargebee events occur
version: '1'
nodeType: trigger
group:
- trigger
params:
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: Any time any event is triggered (Wildcard Event)
  validation:
    required: true
  typeInfo:
    type: multiOptions
    displayName: Events
    name: events
    possibleValues:
    - value: '*'
      name: '*'
      description: Any time any event is triggered (Wildcard Event)
    - value: card_added
      name: Card Added
      description: Triggered when a card is added for a customer
    - value: card_deleted
      name: Card Deleted
      description: Triggered when a card is deleted for a customer
    - value: card_expired
      name: Card Expired
      description: Triggered when the card for a customer has expired
    - value: card_expiring
      name: Card Expiring
      description: Triggered when the customer's credit card is expiring soon.Triggered
        30 days before the expiry date
    - value: card_updated
      name: Card Updated
      description: Triggered when the card is updated for a customer
    - value: customer_changed
      name: Customer Changed
      description: Triggered when a customer is changed
    - value: customer_created
      name: Customer Created
      description: Triggered when a customer is created
    - value: customer_deleted
      name: Customer Deleted
      description: Triggered when a customer is deleted
    - value: invoice_created
      name: Invoice Created
      description: Event triggered (in the case of metered billing) when a 'Pending'
        invoice is created that has usage related charges or line items to be added,
        before being closed. This is triggered only when the “Notify for Pending Invoices”
        option is enabled.
    - value: invoice_deleted
      name: Invoice Deleted
      description: Event triggered when an invoice is deleted
    - value: invoice_generated
      name: Invoice Generated
      description: Event triggered when a new invoice is generated. In case of metered
        billing, this event is triggered when a 'Pending' invoice is closed.
    - value: invoice_updated
      name: Invoice Updated
      description: Triggered when the invoice’s shipping/billing address is updated,
        if the invoice is voided, or when the amount due is modified due to payments
        applied/removed
    - value: payment_failed
      name: Payment Failed
      description: Triggered when attempt to charge customer's credit card fails
    - value: payment_initiated
      name: Payment Initiated
      description: Triggered when a payment is initiated via direct debit
    - value: payment_refunded
      name: Payment Refunded
      description: Triggered when a payment refund is made
    - value: payment_succeeded
      name: Payment Succeeded
      description: Triggered when the payment is successfully collected
    - value: refund_initiated
      name: Refund Initiated
      description: Triggered when a refund is initiated via direct debit
    - value: subscription_activated
      name: Subscription Activated
      description: Triggered after the subscription has been moved from 'Trial' to
        'Active' state
    - value: subscription_cancellation_scheduled
      name: Subscription Cancellation Scheduled
      description: Triggered when subscription is scheduled to cancel at end of current
        term
    - value: subscription_cancelled
      name: Subscription Cancelled
      description: Triggered when the subscription is cancelled. If it is cancelled
        due to non payment or because the card details are not present, the subscription
        will have the possible reason as 'cancel_reason'.
    - value: subscription_cancelling
      name: Subscription Cancelling
      description: Triggered 6 days prior to the scheduled cancellation date
    - value: subscription_changed
      name: Subscription Changed
      description: Triggered when the subscription's recurring items are changed
    - value: subscription_created
      name: Subscription Created
      description: Triggered when a new subscription is created
    - value: subscription_deleted
      name: Subscription Deleted
      description: Triggered when a subscription is deleted
    - value: subscription_reactivated
      name: Subscription Reactivated
      description: Triggered when the subscription is moved from cancelled state to
        'Active' or 'Trial' state
    - value: subscription_renewal_reminder
      name: Subscription Renewal Reminder
      description: Triggered 3 days before each subscription's renewal
    - value: subscription_renewed
      name: Subscription Renewed
      description: Triggered when the subscription is renewed from the current term
    - value: subscription_scheduled_cancellation_removed
      name: Subscription Scheduled Cancellation Removed
      description: Triggered when scheduled cancellation is removed for the subscription
    - value: subscription_shipping_address_updated
      name: Subscription Shipping Address Updated
      description: Triggered when shipping address is added or updated for a subscription
    - value: subscription_started
      name: Subscription Started
      description: Triggered when a 'future' subscription gets started
    - value: subscription_trial_ending
      name: Subscription Trial Ending
      description: Triggered 6 days prior to the trial period's end date
    - value: transaction_created
      name: Transaction Created
      description: Triggered when a transaction is recorded
    - value: transaction_deleted
      name: Transaction Deleted
      description: Triggered when a transaction is deleted
    - value: transaction_updated
      name: Transaction Updated
      description: Triggered when a transaction is updated. E.g. (1) When a transaction
        is removed, (2) or when an excess payment is applied on an invoice, (3) or
        when amount_capturable gets updated.
ui_elements:
  notices: []
  tooltips: []
  placeholders: []
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
  note: Trigger nodes only have common settings (notes, notesInFlow)

```

### JSON Schema

```json
{
  "$id": "https://n8n.io/schemas/nodes/chargebeeTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Chargebee Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "events": {
          "description": "Any time any event is triggered (Wildcard Event)",
          "type": "string",
          "default": []
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
        }
      }
    }
  },
  "metadata": {
    "nodeType": "trigger",
    "version": "1"
  }
}
```

---

## Document Changelog

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1 | 2025-11-13 | Ultimate extraction with maximum detail for AI training |
