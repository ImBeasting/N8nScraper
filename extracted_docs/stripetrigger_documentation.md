---
title: "Node: Stripe Trigger"
slug: "node-stripetrigger"
version: "1"
updated: "2026-01-08"
summary: "Handle Stripe events via webhooks"
node_type: "trigger"
group: "['trigger']"
---

# Node: Stripe Trigger

**Purpose.** Handle Stripe events via webhooks


---

## Node Details

- **Icon:** `file:stripe.svg`
- **Group:** `['trigger']`
- **Inputs:** `[]`
- **Outputs:** `['Main']`

---

## Authentication

- **stripeApi**: N/A


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

## Required Credentials

| Credential Type | Required | Conditions |
| --------------- | -------- | ---------- |
| `stripeApi` | ✓ | - |

---

## Parameters

### Parameters

| Name | Field ID | Type | Default | Required | Description | Validation |
| ---- | -------- | ---- | ------- | :------: | ----------- | ---------- |
| Events | `events` | multiOptions | [] | ✓ | The event to listen to |  |

**Events options:**

* ***** (`*`) - Any time any event is triggered (Wildcard Event)
* **Account Updated** (`account.updated`) - Occurs whenever an account status or property has changed
* **Account Application.authorized** (`account.application.authorized`) - Occurs whenever a user authorizes an application. Sent to the related application only.
* **Account Application.deauthorized** (`account.application.deauthorized`) - Occurs whenever a user deauthorizes an application. Sent to the related application only.
* **Account External_account.created** (`account.external_account.created`) - Occurs whenever an external account is created.
* **Account External_account.deleted** (`account.external_account.deleted`) - Occurs whenever an external account is deleted.
* **Account External_account.updated** (`account.external_account.updated`) - Occurs whenever an external account is updated.
* **Application Fee.created** (`application_fee.created`) - Occurs whenever an application fee is created on a charge.
* **Application Fee.refunded** (`application_fee.refunded`) - Occurs whenever an application fee is refunded, whether from refunding a charge or from refunding the application fee directly. This includes partial refunds.
* **Application Fee.refund.updated** (`application_fee.refund.updated`) - Occurs whenever an application fee refund is updated.
* **Balance Available** (`balance.available`) - Occurs whenever your Stripe balance has been updated (e.g., when a charge is available to be paid out). By default, Stripe automatically transfers funds in your balance to your bank account on a daily basis.
* **Capability Updated** (`capability.updated`) - Occurs whenever a capability has new requirements or a new status.
* **Charge Captured** (`charge.captured`) - Occurs whenever a previously uncaptured charge is captured.
* **Charge Expired** (`charge.expired`) - Occurs whenever an uncaptured charge expires.
* **Charge Failed** (`charge.failed`) - Occurs whenever a failed charge attempt occurs.
* **Charge Pending** (`charge.pending`) - Occurs whenever a pending charge is created.
* **Charge Refunded** (`charge.refunded`) - Occurs whenever a charge is refunded, including partial refunds.
* **Charge Succeeded** (`charge.succeeded`) - Occurs whenever a new charge is created and is successful.
* **Charge Updated** (`charge.updated`) - Occurs whenever a charge description or metadata is updated.
* **Charge Dispute.closed** (`charge.dispute.closed`) - Occurs when a dispute is closed and the dispute status changes to lost, warning_closed, or won.
* **Charge Dispute.created** (`charge.dispute.created`) - Occurs whenever a customer disputes a charge with their bank.
* **Charge Dispute.funds_reinstated** (`charge.dispute.funds_reinstated`) - Occurs when funds are reinstated to your account after a dispute is closed. This includes partially refunded payments.
* **Charge Dispute.funds_withdrawn** (`charge.dispute.funds_withdrawn`) - Occurs when funds are removed from your account due to a dispute.
* **Charge Dispute.updated** (`charge.dispute.updated`) - Occurs when the dispute is updated (usually with evidence).
* **Charge Refund.updated** (`charge.refund.updated`) - Occurs whenever a refund is updated, on selected payment methods.
* **Checkout Session.completed** (`checkout.session.completed`) - Occurs when a Checkout Session has been successfully completed.
* **Coupon Created** (`coupon.created`) - Occurs whenever a coupon is created.
* **Coupon Deleted** (`coupon.deleted`) - Occurs whenever a coupon is deleted.
* **Coupon Updated** (`coupon.updated`) - Occurs whenever a coupon is updated.
* **Credit Note.created** (`credit_note.created`) - Occurs whenever a credit note is created.
* **Credit Note.updated** (`credit_note.updated`) - Occurs whenever a credit note is updated.
* **Credit Note.voided** (`credit_note.voided`) - Occurs whenever a credit note is voided.
* **Customer Created** (`customer.created`) - Occurs whenever a new customer is created.
* **Customer Deleted** (`customer.deleted`) - Occurs whenever a customer is deleted.
* **Customer Updated** (`customer.updated`) - Occurs whenever any property of a customer changes.
* **Customer Discount.created** (`customer.discount.created`) - Occurs whenever a coupon is attached to a customer.
* **Customer Discount.deleted** (`customer.discount.deleted`) - Occurs whenever a coupon is removed from a customer.
* **Customer Discount.updated** (`customer.discount.updated`) - Occurs whenever a customer is switched from one coupon to another.
* **Customer Source.created** (`customer.source.created`) - Occurs whenever a new source is created for a customer.
* **Customer Source.deleted** (`customer.source.deleted`) - Occurs whenever a source is removed from a customer.
* **Customer Source.expiring** (`customer.source.expiring`) - Occurs whenever a card or source will expire at the end of the month.
* **Customer Source.updated** (`customer.source.updated`) - Occurs whenever a source's details are changed.
* **Customer Subscription.created** (`customer.subscription.created`) - Occurs whenever a customer is signed up for a new plan.
* **Customer Subscription.deleted** (`customer.subscription.deleted`) - Occurs whenever a customer's subscription ends.
* **Customer Subscription.trial_will_end** (`customer.subscription.trial_will_end`) - Occurs three days before a subscription's trial period is scheduled to end, or when a trial is ended immediately (using trial_end=now).
* **Customer Subscription.updated** (`customer.subscription.updated`) - Occurs whenever a subscription changes (e.g., switching from one plan to another, or changing the status from trial to active).
* **Customer Tax_id.created** (`customer.tax_id.created`) - Occurs whenever a tax ID is created for a customer.
* **Customer Tax_id.deleted** (`customer.tax_id.deleted`) - Occurs whenever a tax ID is deleted from a customer.
* **Customer Tax_id.updated** (`customer.tax_id.updated`) - Occurs whenever a customer's tax ID is updated.
* **File Created** (`file.created`) - Occurs whenever a new Stripe-generated file is available for your account.
* **Invoice Created** (`invoice.created`) - Occurs whenever a new invoice is created. To learn how webhooks can be used with this event, and how they can affect it, see Using Webhooks with Subscriptions.
* **Invoice Deleted** (`invoice.deleted`) - Occurs whenever a draft invoice is deleted.
* **Invoice Finalized** (`invoice.finalized`) - Occurs whenever a draft invoice is finalized and updated to be an open invoice.
* **Invoice Marked_uncollectible** (`invoice.marked_uncollectible`) - Occurs whenever an invoice is marked uncollectible.
* **Invoice Payment_action_required** (`invoice.payment_action_required`) - Occurs whenever an invoice payment attempt requires further user action to complete.
* **Invoice Payment_failed** (`invoice.payment_failed`) - Occurs whenever an invoice payment attempt fails, due either to a declined payment or to the lack of a stored payment method.
* **Invoice Payment_succeeded** (`invoice.payment_succeeded`) - Occurs whenever an invoice payment attempt succeeds.
* **Invoice Sent** (`invoice.sent`) - Occurs whenever an invoice email is sent out.
* **Invoice Upcoming** (`invoice.upcoming`) - Occurs X number of days before a subscription is scheduled to create an invoice that is automatically charged—where X is determined by your subscriptions settings. Note: The received Invoice object will not have an invoice ID.
* **Invoice Updated** (`invoice.updated`) - Occurs whenever an invoice changes (e.g., the invoice amount).
* **Invoice Voided** (`invoice.voided`) - Occurs whenever an invoice is voided.
* **Invoiceitem Created** (`invoiceitem.created`) - Occurs whenever an invoice item is created.
* **Invoiceitem Deleted** (`invoiceitem.deleted`) - Occurs whenever an invoice item is deleted.
* **Invoiceitem Updated** (`invoiceitem.updated`) - Occurs whenever an invoice item is updated.
* **Issuing Authorization.created** (`issuing_authorization.created`) - Occurs whenever an authorization is created.
* **Issuing Authorization.request** (`issuing_authorization.request`) - Represents a synchronous request for authorization, see Using your integration to handle authorization requests.
* **Issuing Authorization.updated** (`issuing_authorization.updated`) - Occurs whenever an authorization is updated.
* **Issuing Card.created** (`issuing_card.created`) - Occurs whenever a card is created.
* **Issuing Card.updated** (`issuing_card.updated`) - Occurs whenever a card is updated.
* **Issuing Cardholder.created** (`issuing_cardholder.created`) - Occurs whenever a cardholder is created.
* **Issuing Cardholder.updated** (`issuing_cardholder.updated`) - Occurs whenever a cardholder is updated.
* **Issuing Dispute.created** (`issuing_dispute.created`) - Occurs whenever a dispute is created.
* **Issuing Dispute.updated** (`issuing_dispute.updated`) - Occurs whenever a dispute is updated.
* **Issuing Settlement.created** (`issuing_settlement.created`) - Occurs whenever an issuing settlement is created.
* **Issuing Settlement.updated** (`issuing_settlement.updated`) - Occurs whenever an issuing settlement is updated.
* **Issuing Transaction.created** (`issuing_transaction.created`) - Occurs whenever an issuing transaction is created.
* **Issuing Transaction.updated** (`issuing_transaction.updated`) - Occurs whenever an issuing transaction is updated.
* **Order Created** (`order.created`) - Occurs whenever an order is created.
* **Order Payment_failed** (`order.payment_failed`) - Occurs whenever an order payment attempt fails.
* **Order Payment_succeeded** (`order.payment_succeeded`) - Occurs whenever an order payment attempt succeeds.
* **Order Updated** (`order.updated`) - Occurs whenever an order is updated.
* **Order Return.created** (`order_return.created`) - Occurs whenever an order return is created.
* **Payment Intent.amount_capturable_updated** (`payment_intent.amount_capturable_updated`) - Occurs when a PaymentIntent has funds to be captured. Check the amount_capturable property on the PaymentIntent to determine the amount that can be captured. You may capture the PaymentIntent with an amount_to_capture value up to the specified amount. Learn more about capturing PaymentIntents.
* **Payment Intent.canceled** (`payment_intent.canceled`) - Occurs when a PaymentIntent is canceled.
* **Payment Intent.created** (`payment_intent.created`) - Occurs when a new PaymentIntent is created.
* **Payment Intent.payment_failed** (`payment_intent.payment_failed`) - Occurs when a PaymentIntent has failed the attempt to create a source or a payment.
* **Payment Intent.succeeded** (`payment_intent.succeeded`) - Occurs when a PaymentIntent has been successfully fulfilled.
* **Payment Intent.requires_action** (`payment_intent.requires_action`) - Occurs when a PaymentIntent requires an action.
* **Payment Method.attached** (`payment_method.attached`) - Occurs whenever a new payment method is attached to a customer.
* **Payment Method.card_automatically_updated** (`payment_method.card_automatically_updated`) - Occurs whenever a card payment method's details are automatically updated by the network.
* **Payment Method.detached** (`payment_method.detached`) - Occurs whenever a payment method is detached from a customer.
* **Payment Method.updated** (`payment_method.updated`) - Occurs whenever a payment method is updated via the PaymentMethod update API.
* **Payout Canceled** (`payout.canceled`) - Occurs whenever a payout is canceled.
* **Payout Created** (`payout.created`) - Occurs whenever a payout is created.
* **Payout Failed** (`payout.failed`) - Occurs whenever a payout attempt fails.
* **Payout Paid** (`payout.paid`) - Occurs whenever a payout is expected to be available in the destination account. If the payout fails, a payout.failed notification is also sent, at a later time.
* **Payout Updated** (`payout.updated`) - Occurs whenever a payout is updated.
* **Person Created** (`person.created`) - Occurs whenever a person associated with an account is created.
* **Person Deleted** (`person.deleted`) - Occurs whenever a person associated with an account is deleted.
* **Person Updated** (`person.updated`) - Occurs whenever a person associated with an account is updated.
* **Plan Created** (`plan.created`) - Occurs whenever a plan is created.
* **Plan Deleted** (`plan.deleted`) - Occurs whenever a plan is deleted.
* **Plan Updated** (`plan.updated`) - Occurs whenever a plan is updated.
* **Product Created** (`product.created`) - Occurs whenever a product is created.
* **Product Deleted** (`product.deleted`) - Occurs whenever a product is deleted.
* **Product Updated** (`product.updated`) - Occurs whenever a product is updated.
* **Radar Early_fraud_warning.created** (`radar.early_fraud_warning.created`) - Occurs whenever an early fraud warning is created.
* **Radar Early_fraud_warning.updated** (`radar.early_fraud_warning.updated`) - Occurs whenever an early fraud warning is updated.
* **Recipient Created** (`recipient.created`) - Occurs whenever a recipient is created.
* **Recipient Deleted** (`recipient.deleted`) - Occurs whenever a recipient is deleted.
* **Recipient Updated** (`recipient.updated`) - Occurs whenever a recipient is updated.
* **Reporting Report_run.failed** (`reporting.report_run.failed`) - Occurs whenever a requested **ReportRun** failed to complete.
* **Reporting Report_run.succeeded** (`reporting.report_run.succeeded`) - Occurs whenever a requested **ReportRun** completed succesfully.
* **Reporting Report_type.updated** (`reporting.report_type.updated`) - Occurs whenever a **ReportType** is updated (typically to indicate that a new day's data has come available).
* **Review Closed** (`review.closed`) - Occurs whenever a review is closed. The review's reason field indicates why: approved, disputed, refunded, or refunded_as_fraud.
* **Review Opened** (`review.opened`) - Occurs whenever a review is opened.
* **Setup Intent.canceled** (`setup_intent.canceled`) - Occurs when a SetupIntent is canceled.
* **Setup Intent.created** (`setup_intent.created`) - Occurs when a new SetupIntent is created.
* **Setup Intent.setup_failed** (`setup_intent.setup_failed`) - Occurs when a SetupIntent has failed the attempt to setup a payment method.
* **Setup Intent.succeeded** (`setup_intent.succeeded`) - Occurs when an SetupIntent has successfully setup a payment method.
* **Sigma Scheduled_query_run.created** (`sigma.scheduled_query_run.created`) - Occurs whenever a Sigma scheduled query run finishes.
* **Sku Created** (`sku.created`) - Occurs whenever a SKU is created.
* **Sku Deleted** (`sku.deleted`) - Occurs whenever a SKU is deleted.
* **Sku Updated** (`sku.updated`) - Occurs whenever a SKU is updated.
* **Source Canceled** (`source.canceled`) - Occurs whenever a source is canceled.
* **Source Chargeable** (`source.chargeable`) - Occurs whenever a source transitions to chargeable.
* **Source Failed** (`source.failed`) - Occurs whenever a source fails.
* **Source Mandate_notification** (`source.mandate_notification`) - Occurs whenever a source mandate notification method is set to manual.
* **Source Refund_attributes_required** (`source.refund_attributes_required`) - Occurs whenever the refund attributes are required on a receiver source to process a refund or a mispayment.
* **Source Transaction.created** (`source.transaction.created`) - Occurs whenever a source transaction is created.
* **Source Transaction.updated** (`source.transaction.updated`) - Occurs whenever a source transaction is updated.
* **Subscription Schedule.aborted** (`subscription_schedule.aborted`) - Occurs whenever a subscription schedule is canceled due to the underlying subscription being canceled because of delinquency.
* **Subscription Schedule.canceled** (`subscription_schedule.canceled`) - Occurs whenever a subscription schedule is canceled.
* **Subscription Schedule.completed** (`subscription_schedule.completed`) - Occurs whenever a new subscription schedule is completed.
* **Subscription Schedule.created** (`subscription_schedule.created`) - Occurs whenever a new subscription schedule is created.
* **Subscription Schedule.expiring** (`subscription_schedule.expiring`) - Occurs 7 days before a subscription schedule will expire.
* **Subscription Schedule.released** (`subscription_schedule.released`) - Occurs whenever a new subscription schedule is released.
* **Subscription Schedule.updated** (`subscription_schedule.updated`) - Occurs whenever a subscription schedule is updated.
* **Tax Rate.created** (`tax_rate.created`) - Occurs whenever a new tax rate is created.
* **Tax Rate.updated** (`tax_rate.updated`) - Occurs whenever a tax rate is updated.
* **Topup Canceled** (`topup.canceled`) - Occurs whenever a top-up is canceled.
* **Topup Created** (`topup.created`) - Occurs whenever a top-up is created.
* **Topup Failed** (`topup.failed`) - Occurs whenever a top-up fails.
* **Topup Reversed** (`topup.reversed`) - Occurs whenever a top-up is reversed.
* **Topup Succeeded** (`topup.succeeded`) - Occurs whenever a top-up succeeds.
* **Transfer Created** (`transfer.created`) - Occurs whenever a transfer is created.
* **Transfer Failed** (`transfer.failed`) - Occurs whenever a transfer failed.
* **Transfer Paid** (`transfer.paid`) - Occurs after a transfer is paid. For Instant Payouts, the event will be sent on the next business day, although the funds should be received well beforehand.
* **Transfer Reversed** (`transfer.reversed`) - Occurs whenever a transfer is reversed, including partial reversals.
* **Transfer Updated** (`transfer.updated`) - Occurs whenever a transfer's description or metadata is updated.

| API Version | `apiVersion` | string |  | ✗ | The API version to use for requests. It controls the format and structure of the incoming event payloads that Stripe sends to your webhook. If empty, Stripe will use the default API version set in your account at the time, which may lead to event processing issues if the API version changes in the future. | e.g. 2025-05-28.basil |  |

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
* Categories: Finance & Accounting, Sales

---

## Appendix: Machine-Readable Spec (LLM-Friendly)

### YAML Schema

```yaml
node: stripeTrigger
displayName: Stripe Trigger
description: Handle Stripe events via webhooks
version: '1'
nodeType: trigger
group:
- trigger
credentials:
- name: stripeApi
  required: true
params:
- id: events
  name: Events
  type: multiOptions
  default: []
  required: true
  description: The event to listen to
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
    - value: account.updated
      name: Account Updated
      description: Occurs whenever an account status or property has changed
    - value: account.application.authorized
      name: Account Application.authorized
      description: Occurs whenever a user authorizes an application. Sent to the related
        application only.
    - value: account.application.deauthorized
      name: Account Application.deauthorized
      description: Occurs whenever a user deauthorizes an application. Sent to the
        related application only.
    - value: account.external_account.created
      name: Account External_account.created
      description: Occurs whenever an external account is created.
    - value: account.external_account.deleted
      name: Account External_account.deleted
      description: Occurs whenever an external account is deleted.
    - value: account.external_account.updated
      name: Account External_account.updated
      description: Occurs whenever an external account is updated.
    - value: application_fee.created
      name: Application Fee.created
      description: Occurs whenever an application fee is created on a charge.
    - value: application_fee.refunded
      name: Application Fee.refunded
      description: Occurs whenever an application fee is refunded, whether from refunding
        a charge or from refunding the application fee directly. This includes partial
        refunds.
    - value: application_fee.refund.updated
      name: Application Fee.refund.updated
      description: Occurs whenever an application fee refund is updated.
    - value: balance.available
      name: Balance Available
      description: Occurs whenever your Stripe balance has been updated (e.g., when
        a charge is available to be paid out). By default, Stripe automatically transfers
        funds in your balance to your bank account on a daily basis.
    - value: capability.updated
      name: Capability Updated
      description: Occurs whenever a capability has new requirements or a new status.
    - value: charge.captured
      name: Charge Captured
      description: Occurs whenever a previously uncaptured charge is captured.
    - value: charge.expired
      name: Charge Expired
      description: Occurs whenever an uncaptured charge expires.
    - value: charge.failed
      name: Charge Failed
      description: Occurs whenever a failed charge attempt occurs.
    - value: charge.pending
      name: Charge Pending
      description: Occurs whenever a pending charge is created.
    - value: charge.refunded
      name: Charge Refunded
      description: Occurs whenever a charge is refunded, including partial refunds.
    - value: charge.succeeded
      name: Charge Succeeded
      description: Occurs whenever a new charge is created and is successful.
    - value: charge.updated
      name: Charge Updated
      description: Occurs whenever a charge description or metadata is updated.
    - value: charge.dispute.closed
      name: Charge Dispute.closed
      description: Occurs when a dispute is closed and the dispute status changes
        to lost, warning_closed, or won.
    - value: charge.dispute.created
      name: Charge Dispute.created
      description: Occurs whenever a customer disputes a charge with their bank.
    - value: charge.dispute.funds_reinstated
      name: Charge Dispute.funds_reinstated
      description: Occurs when funds are reinstated to your account after a dispute
        is closed. This includes partially refunded payments.
    - value: charge.dispute.funds_withdrawn
      name: Charge Dispute.funds_withdrawn
      description: Occurs when funds are removed from your account due to a dispute.
    - value: charge.dispute.updated
      name: Charge Dispute.updated
      description: Occurs when the dispute is updated (usually with evidence).
    - value: charge.refund.updated
      name: Charge Refund.updated
      description: Occurs whenever a refund is updated, on selected payment methods.
    - value: checkout.session.completed
      name: Checkout Session.completed
      description: Occurs when a Checkout Session has been successfully completed.
    - value: coupon.created
      name: Coupon Created
      description: Occurs whenever a coupon is created.
    - value: coupon.deleted
      name: Coupon Deleted
      description: Occurs whenever a coupon is deleted.
    - value: coupon.updated
      name: Coupon Updated
      description: Occurs whenever a coupon is updated.
    - value: credit_note.created
      name: Credit Note.created
      description: Occurs whenever a credit note is created.
    - value: credit_note.updated
      name: Credit Note.updated
      description: Occurs whenever a credit note is updated.
    - value: credit_note.voided
      name: Credit Note.voided
      description: Occurs whenever a credit note is voided.
    - value: customer.created
      name: Customer Created
      description: Occurs whenever a new customer is created.
    - value: customer.deleted
      name: Customer Deleted
      description: Occurs whenever a customer is deleted.
    - value: customer.updated
      name: Customer Updated
      description: Occurs whenever any property of a customer changes.
    - value: customer.discount.created
      name: Customer Discount.created
      description: Occurs whenever a coupon is attached to a customer.
    - value: customer.discount.deleted
      name: Customer Discount.deleted
      description: Occurs whenever a coupon is removed from a customer.
    - value: customer.discount.updated
      name: Customer Discount.updated
      description: Occurs whenever a customer is switched from one coupon to another.
    - value: customer.source.created
      name: Customer Source.created
      description: Occurs whenever a new source is created for a customer.
    - value: customer.source.deleted
      name: Customer Source.deleted
      description: Occurs whenever a source is removed from a customer.
    - value: customer.source.expiring
      name: Customer Source.expiring
      description: Occurs whenever a card or source will expire at the end of the
        month.
    - value: customer.source.updated
      name: Customer Source.updated
      description: Occurs whenever a source's details are changed.
    - value: customer.subscription.created
      name: Customer Subscription.created
      description: Occurs whenever a customer is signed up for a new plan.
    - value: customer.subscription.deleted
      name: Customer Subscription.deleted
      description: Occurs whenever a customer's subscription ends.
    - value: customer.subscription.trial_will_end
      name: Customer Subscription.trial_will_end
      description: Occurs three days before a subscription's trial period is scheduled
        to end, or when a trial is ended immediately (using trial_end=now).
    - value: customer.subscription.updated
      name: Customer Subscription.updated
      description: Occurs whenever a subscription changes (e.g., switching from one
        plan to another, or changing the status from trial to active).
    - value: customer.tax_id.created
      name: Customer Tax_id.created
      description: Occurs whenever a tax ID is created for a customer.
    - value: customer.tax_id.deleted
      name: Customer Tax_id.deleted
      description: Occurs whenever a tax ID is deleted from a customer.
    - value: customer.tax_id.updated
      name: Customer Tax_id.updated
      description: Occurs whenever a customer's tax ID is updated.
    - value: file.created
      name: File Created
      description: Occurs whenever a new Stripe-generated file is available for your
        account.
    - value: invoice.created
      name: Invoice Created
      description: Occurs whenever a new invoice is created. To learn how webhooks
        can be used with this event, and how they can affect it, see Using Webhooks
        with Subscriptions.
    - value: invoice.deleted
      name: Invoice Deleted
      description: Occurs whenever a draft invoice is deleted.
    - value: invoice.finalized
      name: Invoice Finalized
      description: Occurs whenever a draft invoice is finalized and updated to be
        an open invoice.
    - value: invoice.marked_uncollectible
      name: Invoice Marked_uncollectible
      description: Occurs whenever an invoice is marked uncollectible.
    - value: invoice.payment_action_required
      name: Invoice Payment_action_required
      description: Occurs whenever an invoice payment attempt requires further user
        action to complete.
    - value: invoice.payment_failed
      name: Invoice Payment_failed
      description: Occurs whenever an invoice payment attempt fails, due either to
        a declined payment or to the lack of a stored payment method.
    - value: invoice.payment_succeeded
      name: Invoice Payment_succeeded
      description: Occurs whenever an invoice payment attempt succeeds.
    - value: invoice.sent
      name: Invoice Sent
      description: Occurs whenever an invoice email is sent out.
    - value: invoice.upcoming
      name: Invoice Upcoming
      description: 'Occurs X number of days before a subscription is scheduled to
        create an invoice that is automatically charged—where X is determined by your
        subscriptions settings. Note: The received Invoice object will not have an
        invoice ID.'
    - value: invoice.updated
      name: Invoice Updated
      description: Occurs whenever an invoice changes (e.g., the invoice amount).
    - value: invoice.voided
      name: Invoice Voided
      description: Occurs whenever an invoice is voided.
    - value: invoiceitem.created
      name: Invoiceitem Created
      description: Occurs whenever an invoice item is created.
    - value: invoiceitem.deleted
      name: Invoiceitem Deleted
      description: Occurs whenever an invoice item is deleted.
    - value: invoiceitem.updated
      name: Invoiceitem Updated
      description: Occurs whenever an invoice item is updated.
    - value: issuing_authorization.created
      name: Issuing Authorization.created
      description: Occurs whenever an authorization is created.
    - value: issuing_authorization.request
      name: Issuing Authorization.request
      description: Represents a synchronous request for authorization, see Using your
        integration to handle authorization requests.
    - value: issuing_authorization.updated
      name: Issuing Authorization.updated
      description: Occurs whenever an authorization is updated.
    - value: issuing_card.created
      name: Issuing Card.created
      description: Occurs whenever a card is created.
    - value: issuing_card.updated
      name: Issuing Card.updated
      description: Occurs whenever a card is updated.
    - value: issuing_cardholder.created
      name: Issuing Cardholder.created
      description: Occurs whenever a cardholder is created.
    - value: issuing_cardholder.updated
      name: Issuing Cardholder.updated
      description: Occurs whenever a cardholder is updated.
    - value: issuing_dispute.created
      name: Issuing Dispute.created
      description: Occurs whenever a dispute is created.
    - value: issuing_dispute.updated
      name: Issuing Dispute.updated
      description: Occurs whenever a dispute is updated.
    - value: issuing_settlement.created
      name: Issuing Settlement.created
      description: Occurs whenever an issuing settlement is created.
    - value: issuing_settlement.updated
      name: Issuing Settlement.updated
      description: Occurs whenever an issuing settlement is updated.
    - value: issuing_transaction.created
      name: Issuing Transaction.created
      description: Occurs whenever an issuing transaction is created.
    - value: issuing_transaction.updated
      name: Issuing Transaction.updated
      description: Occurs whenever an issuing transaction is updated.
    - value: order.created
      name: Order Created
      description: Occurs whenever an order is created.
    - value: order.payment_failed
      name: Order Payment_failed
      description: Occurs whenever an order payment attempt fails.
    - value: order.payment_succeeded
      name: Order Payment_succeeded
      description: Occurs whenever an order payment attempt succeeds.
    - value: order.updated
      name: Order Updated
      description: Occurs whenever an order is updated.
    - value: order_return.created
      name: Order Return.created
      description: Occurs whenever an order return is created.
    - value: payment_intent.amount_capturable_updated
      name: Payment Intent.amount_capturable_updated
      description: Occurs when a PaymentIntent has funds to be captured. Check the
        amount_capturable property on the PaymentIntent to determine the amount that
        can be captured. You may capture the PaymentIntent with an amount_to_capture
        value up to the specified amount. Learn more about capturing PaymentIntents.
    - value: payment_intent.canceled
      name: Payment Intent.canceled
      description: Occurs when a PaymentIntent is canceled.
    - value: payment_intent.created
      name: Payment Intent.created
      description: Occurs when a new PaymentIntent is created.
    - value: payment_intent.payment_failed
      name: Payment Intent.payment_failed
      description: Occurs when a PaymentIntent has failed the attempt to create a
        source or a payment.
    - value: payment_intent.succeeded
      name: Payment Intent.succeeded
      description: Occurs when a PaymentIntent has been successfully fulfilled.
    - value: payment_intent.requires_action
      name: Payment Intent.requires_action
      description: Occurs when a PaymentIntent requires an action.
    - value: payment_method.attached
      name: Payment Method.attached
      description: Occurs whenever a new payment method is attached to a customer.
    - value: payment_method.card_automatically_updated
      name: Payment Method.card_automatically_updated
      description: Occurs whenever a card payment method's details are automatically
        updated by the network.
    - value: payment_method.detached
      name: Payment Method.detached
      description: Occurs whenever a payment method is detached from a customer.
    - value: payment_method.updated
      name: Payment Method.updated
      description: Occurs whenever a payment method is updated via the PaymentMethod
        update API.
    - value: payout.canceled
      name: Payout Canceled
      description: Occurs whenever a payout is canceled.
    - value: payout.created
      name: Payout Created
      description: Occurs whenever a payout is created.
    - value: payout.failed
      name: Payout Failed
      description: Occurs whenever a payout attempt fails.
    - value: payout.paid
      name: Payout Paid
      description: Occurs whenever a payout is expected to be available in the destination
        account. If the payout fails, a payout.failed notification is also sent, at
        a later time.
    - value: payout.updated
      name: Payout Updated
      description: Occurs whenever a payout is updated.
    - value: person.created
      name: Person Created
      description: Occurs whenever a person associated with an account is created.
    - value: person.deleted
      name: Person Deleted
      description: Occurs whenever a person associated with an account is deleted.
    - value: person.updated
      name: Person Updated
      description: Occurs whenever a person associated with an account is updated.
    - value: plan.created
      name: Plan Created
      description: Occurs whenever a plan is created.
    - value: plan.deleted
      name: Plan Deleted
      description: Occurs whenever a plan is deleted.
    - value: plan.updated
      name: Plan Updated
      description: Occurs whenever a plan is updated.
    - value: product.created
      name: Product Created
      description: Occurs whenever a product is created.
    - value: product.deleted
      name: Product Deleted
      description: Occurs whenever a product is deleted.
    - value: product.updated
      name: Product Updated
      description: Occurs whenever a product is updated.
    - value: radar.early_fraud_warning.created
      name: Radar Early_fraud_warning.created
      description: Occurs whenever an early fraud warning is created.
    - value: radar.early_fraud_warning.updated
      name: Radar Early_fraud_warning.updated
      description: Occurs whenever an early fraud warning is updated.
    - value: recipient.created
      name: Recipient Created
      description: Occurs whenever a recipient is created.
    - value: recipient.deleted
      name: Recipient Deleted
      description: Occurs whenever a recipient is deleted.
    - value: recipient.updated
      name: Recipient Updated
      description: Occurs whenever a recipient is updated.
    - value: reporting.report_run.failed
      name: Reporting Report_run.failed
      description: Occurs whenever a requested **ReportRun** failed to complete.
    - value: reporting.report_run.succeeded
      name: Reporting Report_run.succeeded
      description: Occurs whenever a requested **ReportRun** completed succesfully.
    - value: reporting.report_type.updated
      name: Reporting Report_type.updated
      description: Occurs whenever a **ReportType** is updated (typically to indicate
        that a new day's data has come available).
    - value: review.closed
      name: Review Closed
      description: 'Occurs whenever a review is closed. The review''s reason field
        indicates why: approved, disputed, refunded, or refunded_as_fraud.'
    - value: review.opened
      name: Review Opened
      description: Occurs whenever a review is opened.
    - value: setup_intent.canceled
      name: Setup Intent.canceled
      description: Occurs when a SetupIntent is canceled.
    - value: setup_intent.created
      name: Setup Intent.created
      description: Occurs when a new SetupIntent is created.
    - value: setup_intent.setup_failed
      name: Setup Intent.setup_failed
      description: Occurs when a SetupIntent has failed the attempt to setup a payment
        method.
    - value: setup_intent.succeeded
      name: Setup Intent.succeeded
      description: Occurs when an SetupIntent has successfully setup a payment method.
    - value: sigma.scheduled_query_run.created
      name: Sigma Scheduled_query_run.created
      description: Occurs whenever a Sigma scheduled query run finishes.
    - value: sku.created
      name: Sku Created
      description: Occurs whenever a SKU is created.
    - value: sku.deleted
      name: Sku Deleted
      description: Occurs whenever a SKU is deleted.
    - value: sku.updated
      name: Sku Updated
      description: Occurs whenever a SKU is updated.
    - value: source.canceled
      name: Source Canceled
      description: Occurs whenever a source is canceled.
    - value: source.chargeable
      name: Source Chargeable
      description: Occurs whenever a source transitions to chargeable.
    - value: source.failed
      name: Source Failed
      description: Occurs whenever a source fails.
    - value: source.mandate_notification
      name: Source Mandate_notification
      description: Occurs whenever a source mandate notification method is set to
        manual.
    - value: source.refund_attributes_required
      name: Source Refund_attributes_required
      description: Occurs whenever the refund attributes are required on a receiver
        source to process a refund or a mispayment.
    - value: source.transaction.created
      name: Source Transaction.created
      description: Occurs whenever a source transaction is created.
    - value: source.transaction.updated
      name: Source Transaction.updated
      description: Occurs whenever a source transaction is updated.
    - value: subscription_schedule.aborted
      name: Subscription Schedule.aborted
      description: Occurs whenever a subscription schedule is canceled due to the
        underlying subscription being canceled because of delinquency.
    - value: subscription_schedule.canceled
      name: Subscription Schedule.canceled
      description: Occurs whenever a subscription schedule is canceled.
    - value: subscription_schedule.completed
      name: Subscription Schedule.completed
      description: Occurs whenever a new subscription schedule is completed.
    - value: subscription_schedule.created
      name: Subscription Schedule.created
      description: Occurs whenever a new subscription schedule is created.
    - value: subscription_schedule.expiring
      name: Subscription Schedule.expiring
      description: Occurs 7 days before a subscription schedule will expire.
    - value: subscription_schedule.released
      name: Subscription Schedule.released
      description: Occurs whenever a new subscription schedule is released.
    - value: subscription_schedule.updated
      name: Subscription Schedule.updated
      description: Occurs whenever a subscription schedule is updated.
    - value: tax_rate.created
      name: Tax Rate.created
      description: Occurs whenever a new tax rate is created.
    - value: tax_rate.updated
      name: Tax Rate.updated
      description: Occurs whenever a tax rate is updated.
    - value: topup.canceled
      name: Topup Canceled
      description: Occurs whenever a top-up is canceled.
    - value: topup.created
      name: Topup Created
      description: Occurs whenever a top-up is created.
    - value: topup.failed
      name: Topup Failed
      description: Occurs whenever a top-up fails.
    - value: topup.reversed
      name: Topup Reversed
      description: Occurs whenever a top-up is reversed.
    - value: topup.succeeded
      name: Topup Succeeded
      description: Occurs whenever a top-up succeeds.
    - value: transfer.created
      name: Transfer Created
      description: Occurs whenever a transfer is created.
    - value: transfer.failed
      name: Transfer Failed
      description: Occurs whenever a transfer failed.
    - value: transfer.paid
      name: Transfer Paid
      description: Occurs after a transfer is paid. For Instant Payouts, the event
        will be sent on the next business day, although the funds should be received
        well beforehand.
    - value: transfer.reversed
      name: Transfer Reversed
      description: Occurs whenever a transfer is reversed, including partial reversals.
    - value: transfer.updated
      name: Transfer Updated
      description: Occurs whenever a transfer's description or metadata is updated.
- id: apiVersion
  name: API Version
  type: string
  default: ''
  required: false
  description: The API version to use for requests. It controls the format and structure
    of the incoming event payloads that Stripe sends to your webhook. If empty, Stripe
    will use the default API version set in your account at the time, which may lead
    to event processing issues if the API version changes in the future.
  placeholder: 2025-05-28.basil
  typeInfo:
    type: string
    displayName: API Version
    name: apiVersion
ui_elements:
  notices: []
  tooltips: []
  placeholders:
  - field: apiVersion
    text: 2025-05-28.basil
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
  "$id": "https://n8n.io/schemas/nodes/stripeTrigger.json",
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Stripe Trigger Node",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "params": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "events": {
          "description": "The event to listen to",
          "type": "string",
          "default": []
        },
        "apiVersion": {
          "description": "The API version to use for requests. It controls the format and structure of the incoming event payloads that Stripe sends to your webhook. If empty, Stripe will use the default API version set in your account at the time, which may lead to event processing issues if the API version changes in the future.",
          "type": "string",
          "default": "",
          "examples": [
            "2025-05-28.basil"
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
        }
      }
    }
  },
  "metadata": {
    "nodeType": "trigger",
    "version": "1"
  },
  "credentials": [
    {
      "name": "stripeApi",
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
